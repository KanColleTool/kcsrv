from constants import *
from db import db, AdmiralQuest, Quest, QuestRequirement
from kancolle.quests import get_quest_progress
from . import AdmiralHelper


def update_quest_progress(quest_id, admiral):
    sql = AdmiralQuest.query.filter_by(quest_id=quest_id, admiral_id=admiral.id)
    admiral_quest = sql.first()
    progress = get_quest_progress(admiral, admiral_quest)
    if progress == QUEST_PROGRESS_100:
        sql.update({"progress": QUEST_PROGRESS_0, "state": QUEST_STATE_COMPLETE})
        db.session.commit()
    elif progress != admiral_quest.progress:
        sql.update({"progress": progress})
        db.session.commit()


def get_questlist_ordered(admiral, exclude_hidden=True):
    """
    Here we get the quest list ordered by category and then by no.
    This is important to make sure we always show Composition->Sortie->Exercise etc
    """
    query = db.session.query(AdmiralQuest, Quest).order_by(Quest.category, Quest.no).filter(
        AdmiralQuest.quest_id == Quest.id, AdmiralQuest.admiral_id == admiral.id)
    if exclude_hidden:
        query = query.filter(AdmiralQuest.state != QUEST_STATE_HIDDEN)

    return query.all()


def unlock_quest(admiral, quest_id):
    db.session.add(AdmiralQuest(admiral_id=admiral.id, quest_id=quest_id))
    db.session.commit()


def complete_quest(admiral, quest_id=None, quest=None):
    query = AdmiralQuest.query.filter_by(quest_id=quest_id, admiral_id=admiral.id)
    admiral_quest = query.first()
    quest = admiral_quest.quest

    AdmiralHelper.admiral_grant_resources(admiral, quest.reward)

    api_response = {}
    api_response['api_material'] = quest.reward.to_list()
    api_response["api_bounus_count"] = quest.bonuses.count()
    api_response["api_bounus"] = []
    for bonus in quest.bonuses.all():
        """
        TODO unlock Fleet, LSC, etc.
        Also, I still can't get the effect announcing bonus items. They are added to Admiral's inventory,
        but the bonus reward announcent doesn't show up.
        """
        api_bonus = {
            "api_type": bonus.kind, "api_count": bonus.quantity
        }
        if bonus.kind == QUEST_REWARD_SHIP:
            ship = bonus.ship
            api_bonus["api_item"] = {
                "api_ship_id": ship.id, "api_name": ship.name, "api_getmes": ship.getmsg
            }
            AdmiralHelper.admiral_grant_ship(admiral, ship.id, bonus.quantity)
        elif bonus.kind == QUEST_REWARD_ITEM:
            api_bonus["api_item"] = {
                "api_id": bonus.item_id, "api_name": ""
            }
            AdmiralHelper.admiral_grant_item(admiral, bonus.item_id, bonus.quantity)
        api_response["api_bounus"].append(api_bonus)

    db.session.query(AdmiralQuest).filter(AdmiralQuest.id == admiral_quest.id).update(
        {"state": QUEST_STATE_HIDDEN, "progress": QUEST_PROGRESS_0})
    db.session.commit() # Er...

    """Unlocking new quests"""
    list_maybe_unlocked = db.session.query(QuestRequirement).filter(QuestRequirement.required_id == quest.id).all()
    for maybe_unlocked in list_maybe_unlocked:
        """maybe_unlocked -> requires quest just completed, so it may be unlocked"""
        id_quest_maybe = maybe_unlocked.quest_id
        quests_required = db.session.query(QuestRequirement).filter(QuestRequirement.quest_id == id_quest_maybe).all()
        """quests_required -> all quests required to unlock maybe_unlocked"""
        number_required = len(quests_required)
        if number_required == 1:
            """We just completed the one needed, so might as well save one query"""
            unlock_quest(admiral, id_quest_maybe)
            break
        ids_required = [quest.required_id for quest in quests_required]
        """
        This basically checks if all quests_required have the state QUEST_STATE_HIDDEN.
        If the quest is missing from the list or is not marked as hidden, then the quest can't be unlocked.
        """
        quest_count = db.session.query(AdmiralQuest).filter(AdmiralQuest.state == QUEST_STATE_HIDDEN,
            AdmiralQuest.quest_id.in_(ids_required)).count()
        if number_required == quest_count:
            unlock_quest(admiral, quest_id)
    return api_response
