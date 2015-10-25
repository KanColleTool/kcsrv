from constants import *
from db import db, AdmiralQuest
from kancolle.quests import get_quest_progress


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



