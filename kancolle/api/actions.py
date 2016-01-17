from flask import request, g, Blueprint
from db import db
from helpers import _QuestHelper, AdmiralHelper, DockHelper
from util import svdata, prepare_api_blueprint

from util import svdata
from db import db, Kanmusu
from helpers import ActionsHelper


api_actions = Blueprint('api_actions', __name__)


@api_actions.route('/api_port/port', methods=['GET', 'POST'])
def port():
    return svdata(ActionsHelper.port())


@api_actions.route('/api_req_kaisou/slotset', methods=['GET', 'POST'])
# Change Item
def slotset():
    id = request.values.get("api_id")
    equip_id = request.values.get("api_item_id")
    slot = request.values.get("api_slot_idx")

    Kanmusu.get(id).equip(admiral_equip_id=equip_id, slot=slot)
    db.session.commit()
    return svdata({})


@api_actions.route('/api_req_kaisou/powerup', methods=['GET', 'POST'])
# Modernization
def powerup():
    id = request.values.get("api_id")
    id_items = request.values.get("api_id_items").split(',')  # How mean girls aren't items
    result = Kanmusu.get(id).modernize(id_items)
    db.session.commit()
    return svdata(ActionsHelper.powerup(id, result))


@api_actions.route('/api_req_kaisou/remodeling', methods=['GET', 'POST'])
# Remodeling
def remodeling():
    id = request.values.get("api_id")
    Kanmusu.get(id).remodel()  # If it only were that easy...
    return svdata({})


""""" Refit End """""


@api_actions.route('/api_req_hensei/lock', methods=['POST'])
def lock():
    """Heartlock/unheartlock a ship."""
    admiral = g.admiral
    admiralship = admiral.kanmusu.filter_by(local_ship_num=int(request.values.get("api_ship_id")) - 1).first()

    locked = not admiralship.heartlocked

    admiralship.heartlocked = locked
    db.session.add(admiralship)
    db.session.commit()
    return svdata({"api_locked": int(locked)})


@api_actions.route('/api_req_kousyou/createship', methods=['POST'])
def build():
    fuel = int(request.values.get("api_item1"))
    ammo = int(request.values.get("api_item2"))
    steel = int(request.values.get("api_item3"))
    baux = int(request.values.get("api_item4"))
    dock = int(request.values.get("api_kdock_id")) # -1 # For some reason, it doesn't need minusing one. ¯\_(ツ)_/¯
    DockHelper.craft_ship(fuel, ammo, steel, baux, dock)
    return svdata({})


@api_actions.route('/api_req_kousyou/getship', methods=['POST'])
def getship():
    dock = int(request.values.get("api_kdock_id"))
    try:
        data = _DockHelper.get_and_remove_ship(dockid=dock)
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


@api_actions.route('/api_req_quest/start', methods=['GET', 'POST'])
# Start quest
def queststart():
    admiral = get_token_admiral_or_error()
    quest_id = request.values.get("api_quest_id")
    AdmiralHelper.activate_quest(quest_id, admiral)
    _QuestHelper.update_quest_progress(quest_id, admiral)
    return svdata({'api_result_msg': 'ok', 'api_result': 1})


@api_actions.route('/api_req_quest/stop', methods=['GET', 'POST'])
# Stop quest
def queststop():
    admiral = get_token_admiral_or_error()
    quest_id = request.values.get("api_quest_id")
    AdmiralHelper.deactivate_quest(quest_id, admiral)
    return svdata({'api_result_msg': 'ok', 'api_result': 1})


@api_actions.route('/api_req_quest/agclearitemget', methods=['GET', 'POST'])
# Complete quest
def clearitemget():
    admiral = get_token_admiral_or_error()
    quest_id = request.values.get("api_quest_id")
    data = _QuestHelper.complete_quest(admiral, quest_id)
    return svdata(data)

api_user = Blueprint('api_user', __name__)
prepare_api_blueprint(api_user)

@api_user.route("/api_get_member/charge", methods=["GET", "POST"])
def resupply():
    # Get the ships. Misleading name of the year candidate.
    ships = request.values.get("api_id_items")
    ships = ships.split(',')
    # New dict for api_ships
    api_ships = {}
    for ship_id in ships:
        ship = Kanmusu.query.filter(Admiral.id == g.admiral.id, Kanmusu.number == ship_id).first_or_404()
        # Assertion for autocompletion in pycharm
        assert isinstance(ship, Kanmusu)
        # Calculate requirements.
        # Follows this formula: how many bars they use x 10% x their fuel/ammo cost


#@api_user.route('/api_get_member/material', methods=['GET', 'POST'])
#def material():
#    """Resources such as fuel, ammo, etc..."""
#    admiral = get_token_admiral_or_error()
#    return svdata(gamestart.get_admiral_resources_api_data(admiral))


#api_user.route('/api_get_member/mapinfo', methods=['GET', 'POST'])
#def mapinfo():
#    return svdata(_AdmiralHelper.get_admiral_sorties())


@api_user.route('/api_get_member/questlist', methods=['GET', 'POST'])
# My god, he rebuilds the questlist every time you (de)activate a quest...
def questlist():
    import math
    page_number = request.values.get('api_page_no', None)
    data = {}
    admiral = get_token_admiral_or_error()
    questlist = QuestHelper.get_questlist_ordered(admiral)
    data['api_count'] = len(questlist)
    data['api_page_count'] = int(math.ceil(data['api_count'] / 5))
    data["api_disp_page"] = int(page_number)
    data["api_list"] = []
    for admiral_quest, quest in questlist:
        data["api_list"].append({
            "api_no": quest.id, "api_category": quest.category, "api_type": quest.frequency, "api_state": admiral_quest.state, "api_title": quest.title, "api_detail": quest.detail, "api_get_material": quest.reward.to_list(), "api_bonus_flag": quest.bonus_flag, "api_progress_flag": admiral_quest.progress, "api_invalid_flag": quest.invalid_flag
        })
    return svdata(data)


@api_user.route('/api_get_member/ship3', methods=['GET', 'POST'])
# Heh
def ship3():
    admiral = get_token_admiral_or_error()
    # No idea.
    # spi_sort_order = request.values.get('spi_sort_order')
    # spi_sort_order = request.values.get('api_sort_key')
    admiral_ship_id = request.values.get('api_shipid')
    data = {
        "api_ship_data": [_ShipHelper.get_admiral_ship_api_data(
            admiral_ship_id)], "api_deck_data": AdmiralHelper.get_admiral_deck_api_data(
            admiral), "api_slot_data": _ItemHelper.get_slottype_list(admiral=admiral)
    }
    return svdata(data)


@api_user.route('/api_get_member/test', methods=['GET', 'POST'])
def test():
    return svdata({})


# Generic routes for anything not implemented.

@api_user.route('/api_req_init/<path:path>', methods=['GET', 'POST'])
def misc(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201})


@api_user.route('/api_get_member/<path:path>', methods=['GET', 'POST'])
def misc2(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201})
