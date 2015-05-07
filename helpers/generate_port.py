import time

import db
import util
from helpers import AdmiralHelper, LevelHelper


def generate_port(api_token):
    # First, get the admiral.
    admiral = util.get_token_admiral_or_error(api_token)
    assert isinstance(admiral, db.Admiral)
    # Initial KanColle reply.
    port2 = {
        "api_result_msg": "成功",
        "api_result": 1,
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
    # port2["api_data"]["api_parallel_quest_count"] = 5
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
    # Fleets.
    for fleet in admiral.fleets.all():
        count += 1
        ships = [n+1 for n, _ in enumerate(fleet.ships.all())]
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
    port2['api_data']['api_materials'] = [
        {"api_id": n + 1,
         "api_member_id": admiral.id,
         "api_value": int(val)} for n, val in enumerate(admiral.resources.split(','))
    ]
    # Ships! Yay! (said nobody)
    port2['api_data']['api_ship'] = []
    # Generate the absolute clusterfuck.
    # count = 0
    for num, ship in enumerate(admiral.admiral_ships.all()):
        # count += 1
        assert isinstance(ship, db.AdmiralShip)
        temp_dict = {
            'api_onslot': [0, 0, 0, 0, 0],
            'api_locked_equip': 0,
            'api_bull': ship.ammo,
            'api_soukou': [ship.armour, ship.ship.armour_max],
            'api_locked': ship.heartlocked,
            'api_nowhp': ship.current_hp,
            'api_raisou': [ship.torpedo_eq, ship.ship.torpedo_max],
            'api_lv': ship.level,
            'api_slotnum': ship.ship.maxslots,
            'api_srate': 1,  # TODO: Implement stars
            'api_cond': ship.fatigue,
            'api_kaihi': [ship.evasion, ship.ship.evasion_max],
            'api_sortno': ship.ship.number,
            'api_fuel': ship.fuel,
            'api_taiku': [ship.antiair_eq, ship.ship.antiair_max],
            'api_leng': ship.ship.srange,
            'api_taisen': [ship.antisub, ship.ship.antisub_base],
            # Guesswork on exp part.
            'api_exp': [ship.exp, LevelHelper.get_exp_required(ship.level, ship.exp), 0],
            'api_slot': [-1, -1, -1, -1, -1],  # TODO: implement items
            'api_backs': ship.ship.rarity,
            'api_sally_area': 0,  # dunno
            'api_ndock_item': list(map(int, util.take_items(ship.repair_base.split(','), [1, 3]))),
            'api_id': num+1,  # temporary
            'api_karyoku': [ship.firepower_eq, ship.ship.firepower_max],
            'api_maxhp': ship.ship.maxhp,
            'api_lucky': [ship.luck_eq, ship.ship.luck_max],
            'api_ship_id': ship.ship.id,
            'api_ndock_time': 0,
            'api_kyouka': [0, 0, 0, 0, 0]
        }
        port2['api_data']['api_ship'].append(temp_dict)
    # Generate ndock.
    docks = admiral.repair_docks.all()
    port2['api_data']['api_ndock'] = []
    for x in range(0, 4):
        if len(docks) - 1 >= x:
            dock = docks[x]
            temp_dict = {
                'api_state': dock.state,
                'api_created_ship_id': dock.ship,
                'api_complete_time': dock.complete,
                'api_complete_time_str': time.strftime("%Y-%m-%d %X"),
                'api_item1': dock.fuel,
                'api_item2': dock.ammo,
                'api_item3': dock.steel,
                'api_item4': dock.baux
            }
        else:
            temp_dict = {
                'api_state': 0,
                'api_created_ship_id': 0,
                'api_complete_time': 0,
                'api_complete_time_str': "0",
                'api_item1': 0,
                'api_item2': 0,
                'api_item3': 0,
                'api_item4': 0,
            }
        temp_dict['api_id'] = x+1
        temp_dict['api_member_id'] = admiral.id
        port2['api_data']['api_ndock'].append(temp_dict)
    return port2