from db import db,Admiral,AdmiralQuest,Quest,Ship
from constants import  *

def ship_add(admiral_id,ship_id):
    admiral = db.session.query(Admiral).get(admiral_id)
    admiral.add_kanmusu(ship_id)
    ship = db.session.query(Ship).get(ship_id)
    print("Ship {} added to Admiral {}".format(ship.name,admiral.id))

def quest_add(admiral_id,quest_id):
    admiral = db.session.query(Admiral).get(admiral_id)
    QuestHelper.unlock_quest(admiral,quest_id)
    print("Eh, if id was correct it probably worked.")

def quest_complete(admiral_id,quest_id):
    db.session.query(AdmiralQuest).filter(Admiral.id==admiral_id,Quest.id==quest_id)\
        .update({"state":QUEST_STATE_COMPLETE})
    db.session.commit()
    print("Eh, if id was correct it probably worked.")

def item_add(admiral,item_id):
    db.session.add(AdmiralItem(admiral_id = admiral.id,item_id = item_id))
    db.session.commit()
    print("Eh, if id was correct it probably worked.")