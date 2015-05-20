import db
import util
from helpers import AdmiralHelper, ShipHelper, DockHelper


def generate_port(api_token):
    # First, get the admiral.
    admiral = util.get_token_admiral_or_error(api_token)
    assert isinstance(admiral, db.Admiral)
    # Initial KanColle reply.
    port2 = {
        "api_data": {}
    }
    # TODO: Log entry
    port2["api_data"]['api_log'] = [
        {
            "api_state": "0",
            "api_no": 0,
            "api_type": "1",
            "api_message": "ayy lmao"
        }
    ]
    # Background music?
    port2["api_data"]["api_p_bgm_id"] = 100
    # This sets the parallel quest count. Don't know what higher values do, default is 5.
    # I set it to ten because fuck the police
    port2["api_data"]["api_parallel_quest_count"] = 10
    # Combined flag? Event data probably.
    port2["api_data"]["api_combined_flag"] = 0
    # API basic - a replica of api_get_member/basic
    basic = AdmiralHelper.get_admiral_basic_info()
    port2['api_data']['api_basic'] = util.merge_two_dicts(basic,
        {
            'api_medals': 0,
            'api_large_dock': 0
        })
    port2['api_data']['api_deck_port'] = []
    count = 0
    # Sort the admiral ships list. Not even sure if this is needed...
    admiral_ships = sorted(admiral.admiral_ships.all(), key=lambda x: x.local_ship_num)

    # Fleets.
    for fleet in admiral.fleets.all():
        count += 1
        ships = [ship.local_ship_num+1 for ship in fleet.ships.all() if ship is not None]
        temp_dict = {
            # Unknown value, always zero for some reason.
            'api_flagship': 0,
            # The Admiral ID, presumably.
            'api_member_id': admiral.id,
            # The name of the fleet.
            'api_name': fleet.name,
            # Unknown value, always empty.
            'api_name_id': "",
            # The local fleet ID.
            'api_id': count,
            # List of ships.
            "api_ship": ships + [-1] * (6 - len(ships)),
            # Mission data?
            "api_mission": [0, 0, 0, 0]
        }

        port2['api_data']['api_deck_port'].append(temp_dict)
    # Materials.
    port2['api_data']['api_material'] = [
        {"api_id": n + 1,
         "api_member_id": admiral.id,
         "api_value": int(val)} for n, val in enumerate(admiral.resources.split(','))
    ]
    port2['api_data']['api_ship'] = []
    # Ship data, Luckily this is generated for us by a helper class.
    for num, ship in enumerate(admiral_ships):
        if not ship.active:
            continue
        assert isinstance(ship, db.AdmiralShip)
        port2['api_data']['api_ship'].append(ShipHelper.generate_api_data(admiral.id, ship.local_ship_num))
    # Generate ndock.
    port2['api_data']['api_ndock'] = DockHelper.generate_dock_data(admiral)['rdock']
    return port2