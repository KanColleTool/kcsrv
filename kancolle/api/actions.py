import traceback
from flask import request, g, Blueprint, abort
import helpers.MemberHelper
from db import Admiral, Expedition
from db import db, Kanmusu
from helpers import _QuestHelper, AdmiralHelper, DockHelper, MemberHelper
from util import prepare_api_blueprint
from util import svdata

api_actions = Blueprint('api_actions', __name__)

import logging

logger = logging.getLogger("kcsrv")


@api_actions.route('/api_port/port', methods=['GET', 'POST'])
def port():
    return svdata(helpers.MemberHelper.port())


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
    return svdata(MemberHelper.powerup(id, result))


@api_actions.route('/api_req_kaisou/remodeling', methods=['GET', 'POST'])
# Remodeling
def remodeling():
    id = request.values.get("api_id")
    Kanmusu.get(id).remodel()  # If it only were that easy...
    return svdata({})


@api_actions.route('/api_req_hensei/lock', methods=['POST'])
def lock():
    """Heartlock/unheartlock a ship."""
    try:
        kanmusu = g.admiral.kanmusu[int(request.values.get("api_ship_id")) - 1]
    except IndexError:
        abort(404)
        return
    except ValueError:
        abort(400)
        return
    kanmusu.locked = not kanmusu.locked

    db.session.add(kanmusu)
    db.session.commit()
    return svdata({"api_locked": int(kanmusu.locked)})


@api_actions.route('/api_req_kousyou/createship', methods=['POST'])
def build():
    fuel = int(request.values.get("api_item1"))
    ammo = int(request.values.get("api_item2"))
    steel = int(request.values.get("api_item3"))
    baux = int(request.values.get("api_item4"))
    dock = int(request.values.get("api_kdock_id")) - 1
    DockHelper.craft_ship(fuel, ammo, steel, baux, dock)
    return svdata({})


@api_actions.route('/api_req_kousyou/getship', methods=['POST'])
def getship():
    dock = int(request.values.get("api_kdock_id")) - 1
    data = DockHelper.get_and_remove_ship_kdock(dockid=dock)
    return svdata(data)


@api_actions.route("/api_req_hokyu/charge", methods=["GET", "POST"])
def resupply():
    # Get the ships. Misleading name of the year candidate.
    ships = request.values.get("api_id_items")
    ships = ships.split(',')
    ships = [int(_) for _ in ships]
    # Get kind.
    kind = int(request.values.get("api_kind"))
    api_ship = []
    # New dict for api_ships
    for ship_id in ships:
        ship = Kanmusu.query.filter(Admiral.id == g.admiral.id, Kanmusu.number == ship_id).first_or_404()
        # Assertion for autocompletion in pycharm
        assert isinstance(ship, Kanmusu)
        # Calculate requirements.
        # Simply replenish up to the maximum stats amount.
        if kind == 1:
            g.admiral.resources.sub(ship.stats.fuel - ship.current_fuel, 0, 0, 0)
            ship.current_fuel = ship.stats.fuel
        elif kind == 2:
            g.admiral.resources.sub(0, ship.stats.ammo - ship.current_ammo, 0, 0)
            ship.current_ammo = ship.stats.ammo
        elif kind == 3:
            g.admiral.resources.sub(ship.stats.fuel - ship.current_fuel, 0, 0, 0)
            ship.current_fuel = ship.stats.fuel
            g.admiral.resources.sub(0, ship.stats.ammo - ship.current_ammo, 0, 0)
            ship.current_ammo = ship.stats.ammo
        api_ship.append({
            "api_id": ship.number,
            "api_fuel": ship.current_fuel,
            "api_bull": ship.current_ammo,
            "api_onslot": [0, 0, 0, 0, 0]  # ???
        })
        db.session.add(ship)
    db.session.add(g.admiral)
    db.session.commit()
    return svdata({"api_ship": api_ship, "api_material": g.admiral.resources.to_list()})


@api_actions.route('/api_req_hensei/change', methods=['GET', 'POST'])
def change_pos():
    # This is a lot cleaner than before.
    # Known bug: You cannot switch sometimes properly, when changing ship with one in your library.
    # Get data from request.
    fleet_id = int(request.values.get("api_id")) - 1
    ship_id = int(request.values.get("api_ship_id")) - 1
    ship_pos = int(request.values.get("api_ship_idx"))

    if ship_pos > 5:
        abort(400)
    if fleet_id > 4:
        abort(400)

    # Get the fleet.
    try:
        fleet = g.admiral.fleets[fleet_id]
    except IndexError:
        logger.warn("Admiral -> {} / Fleet ID -> {} / IndexError".format(g.admiral, fleet_id))
        abort(404)
        return

    # Find the ship with id `ship_id`.
    try:
        if ship_id != -2:
            kmsu = g.admiral.kanmusu[ship_id]
        else:
            kmsu = None
    except:
        logger.warn("Admiral -> `{}` / Ship ID -> `{}` / IndexError".format(g.admiral, ship_id))
        abort(404)
        return

    # Finally, get the ship at `ship_pos` of fleet.
    try:
        kmsu2 = fleet.kanmusu[ship_pos]
    except IndexError:
        kmsu2 = None

    # Check if it's already in the fleet.
    if kmsu and not kmsu in fleet.kanmusu:
        kmsu.fleet_position = len(fleet.kanmusu)
        fleet.kanmusu.append(kmsu)
        db.session.add(kmsu)
        db.session.commit()
        return svdata({})

    if kmsu:
        current_ship_pos = kmsu.fleet_position
    elif kmsu2:
        current_ship_pos = kmsu2.fleet_position
    else:
        current_ship_pos = None

    # Check if it's a removal.
    if ship_id == -2:
        # We cannot use the loaded `kmsu`. This was actually the root cause of #19 and #21, I believe.
        # However, we already have it loaded, at `kmsu2`, because Kancolle is stupid.
        kmsu = kmsu2
        # Bump the other ship numbers down.
        for kanmusu in fleet.kanmusu:
            if kanmusu == kmsu:
                pass
            elif kanmusu.fleet_position is None:
                print("Unknown error - fleet position is None, yet it's still in the fleet?!?")
                print("ID - {}".format(kanmusu.id))
                # Fix fleet position to be 5, at least temporarily.
                kanmusu.fleet_position = 5
            elif current_ship_pos is None:
                # .
                # I what
                # You're trying to remove a ship
                # That doesn't exist
                kanmusu.fleet_position -= 1
            elif kanmusu.fleet_position > current_ship_pos:
                kanmusu.fleet_position -= 1
                db.session.add(kanmusu)
        # Remove fleet position
        kmsu.fleet_position = None
        # Remove from fleet
        fleet.kanmusu.remove(kmsu)
        # Add to session
        db.session.add(fleet)
        db.session.add(kmsu)
        db.session.commit()
        return svdata({})

    print(ship_pos, current_ship_pos)
    # Change fleet position of kanmusu 1.
    kmsu.fleet_position = ship_pos
    # Change fleet position of kanmusu 2, if applicable.
    if kmsu2:
        kmsu2.fleet_position = current_ship_pos
    db.session.add(kmsu, kmsu2)
    db.session.commit()
    return svdata({})


api_user = Blueprint('api_user', __name__)
prepare_api_blueprint(api_user)


@api_user.route('/api_get_member/ship3', methods=['GET', 'POST'])
# Heh
def ship3():
    admiral = g.admiral
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


# Generic routes for anything not implemented.

@api_user.route('/api_req_init/<path:path>', methods=['GET', 'POST'])
def misc(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201}), 404


@api_user.route('/api_get_member/<path:path>', methods=['GET', 'POST'])
def misc2(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201}), 404
