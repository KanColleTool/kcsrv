from db import db,Admiral,AdmiralQuest,Quest,AdmiralItem,Ship
from constants import  *
from helpers import ShipHelper,QuestHelper

def ship_add(admiral_id,ship_id):
    """
    This is going to crash the game after 4 uses because tThe method adds a new fleet every time it's called.
    I could fix it, be we'll refactor most of this really soon, so I can't be bothered.
    """
    admiral = db.session.query(Admiral).get(admiral_id)
    ship = db.session.query(Ship).get(ship_id)
    if ship is not None:
        ShipHelper.assign_ship(admiral,ship_id)
        db.session.commit()
        print("Ship {} added to Admiral {}".format(ship.name,admiral.id))
    else:
        print("Ship id {} not found".format(ship_id))

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