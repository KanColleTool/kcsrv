from flask import request, Blueprint

from db import db
from helpers import DockHelper, ShipHelper,AdmiralHelper,QuestHelper
from util import get_token_admiral_or_error, svdata, prepare_api_blueprint

api_actions = Blueprint('api_actions', __name__)
prepare_api_blueprint(api_actions)


@api_actions.route('/api_req_hensei/lock', methods=['POST'])
def lock():
    """Heartlock/unheartlock a ship."""
    admiral = get_token_admiral_or_error()
    admiralship = admiral.admiral_ships.filter_by(local_ship_num=int(request.values.get("api_ship_id")) - 1).first()

    locked = not admiralship.heartlocked

    admiralship.heartlocked = locked
    db.session.add(admiralship)
    db.session.commit()
    return svdata({"api_locked": int(locked)})


@api_actions.route('/api_req_kousyou/createship', methods=['POST'])
def build():
    admiral = get_token_admiral_or_error()
    fuel = int(request.values.get("api_item1"))
    ammo = int(request.values.get("api_item2"))
    steel = int(request.values.get("api_item3"))
    baux = int(request.values.get("api_item4"))
    dock = int(request.values.get("api_kdock_id")) # -1 # For some reason, it doesn't need minusing one. ¯\_(ツ)_/¯
    DockHelper.craft_ship(fuel, ammo, steel, baux, admiral, dock)
    return svdata({})


@api_actions.route('/api_req_kousyou/getship', methods=['POST'])
def getship():
    dock = int(request.values.get("api_kdock_id"))
    try:
        data = DockHelper.get_and_remove_ship(dockid=dock)
    except (IndexError, AttributeError):
        return svdata({}, code=201, message='申し訳ありませんがブラウザを再起動し再ログインしてください。')
    return svdata(data)


@api_actions.route('/api_req_hensei/change', methods=['GET', 'POST'])
def change_position():
    # TODO UNFUCK THIS CODE UP
    admiral = get_token_admiral_or_error()
    # Get request parameters
    fleet_id = int(request.values.get("api_id")) - 1
    ship_id = int(request.values.get("api_ship_id")) - 1
    ship_pos = int(request.values.get("api_ship_idx"))
    fleet = admiral.fleets.all()[fleet_id]
    fships = fleet.ships.all()

    print(ship_id, ship_pos)
    if ship_id == -2:
        # Delete ship.
        oldship = fships[ship_pos]
        oldship.local_fleet_num = None
        fships.remove(oldship)
        # Get the rest of the ships, and bump it down.
        for n, ship in enumerate(fships):
            if n > ship_id:
                ship.local_fleet_num -= 1
                fships[n] = ship
        fleet.ships = fships
    elif len(fships) == ship_pos:
        # Append to the ships list
        if admiral.admiral_ships.filter_by(local_ship_num=ship_id).first() in fships:
            pass
        else:
            # Get the first ship, update the local fleet num, and append it to the fleet.
            nship = admiral.admiral_ships.filter_by(local_ship_num=ship_id).first()
            nship.local_fleet_num = ship_pos
            fships.append(nship)
            fleet.ships = fships
    else:
        # Get the original ship.
        original_ship = fships[ship_pos]
        # Get the new ship.
        new_ship = fleet.ships.filter_by(local_ship_num=ship_id).first()
        if new_ship is None:
            # BLEH
            original_ship.local_fleet_num = None
            original_ship.fleet_id = None
            db.session.add(original_ship)
            new_ship = admiral.admiral_ships.filter_by(local_ship_num=ship_id).first()
            new_ship.local_fleet_num = ship_pos
            fleet.ships.append(new_ship)
            db.session.add(fleet)
            db.session.commit()
            return svdata({})
        # Do the bullshit swap.
        original_ship.local_fleet_num, new_ship.local_fleet_num = new_ship.local_fleet_num, original_ship.local_fleet_num
        # Eww, merge ships back into the admiral_ships table
        db.session.add(original_ship)
        db.session.add(new_ship)

    # Update the fleet.
    db.session.add(fleet)
    db.session.commit()
    return svdata({})


@api_actions.route('/api_req_init/firstship', methods=['GET', 'POST'])
# Kancolle literally doesn't care, as long as it gets something back
def firstship():
    admiral = get_token_admiral_or_error()
    if admiral.setup:
        return svdata({'api_result_msg': "Nice try.", 'api_result': 200})
    shipid = request.values.get("api_ship_id")
    ShipHelper.assign_ship(admiral, shipid)

    admiral.setup = True

    db.session.add(admiral)
    db.session.commit()
    return svdata({'api_result_msg': 'shitty api is shitty', 'api_result': 1})

@api_actions.route('/api_req_quest/start', methods=['GET', 'POST'])
# Start quest
def queststart():
    admiral = get_token_admiral_or_error()
    quest_id = request.values.get("api_quest_id")
    AdmiralHelper.activate_quest(quest_id,admiral)
    QuestHelper.update_quest_progress(quest_id,admiral)
    return svdata({'api_result_msg': 'ok', 'api_result': 1})

@api_actions.route('/api_req_quest/stop', methods=['GET', 'POST'])
# Stop quest
def queststop():
    admiral = get_token_admiral_or_error()
    quest_id = request.values.get("api_quest_id")
    AdmiralHelper.deactivate_quest(quest_id,admiral)
    return svdata({'api_result_msg': 'ok', 'api_result': 1})

@api_actions.route('/api_req_quest/clearitemget', methods=['GET', 'POST'])
# Complete quest
def clearitemget():
    admiral = get_token_admiral_or_error()
    quest_id = request.values.get("api_quest_id")
    data = QuestHelper.complete_quest(admiral,quest_id)
    return svdata(data)

@api_actions.route('/api_req_kaisou/slotset', methods=['GET', 'POST'])
# Change Item
def slotset():
    admiral = get_token_admiral_or_error()
    admiral_ship_id = request.values.get("api_id")
    admiral_item_id = request.values.get("api_item_id")
    slot = request.values.get("api_slot_idx")    
    ShipHelper.change_ship_item(admiral_ship_id,admiral_item_id,slot)
    return svdata({'api_result_msg': 'ok', 'api_result': 1})