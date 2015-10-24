import datetime
import time

from flask import g

from . import LevelHelper


def kanmusu(kanmusu):
    ship = kanmusu.ship

    # AdmiralShip *must have* entries in AdmiralShipItem table, or we catbomb.
    equips = [equip.admiral_equipment.equipment_id if equip.admiral_equipment_id else -1 for equip in kanmusu.equipment]

    kanmusu_data = {
        'api_id': kanmusu.id, 'api_ship_id': ship.api_id,
    # This must match api_data2 or we get different Ships in the game and DB.
        'api_onslot': [0, 0, 0, 0, 0], # ?
        'api_locked_equip': 0, 'api_bull': kanmusu.current_ammo, 'api_soukou': [kanmusu.stats.armour,
            ship.max_stats.armour], 'api_locked': kanmusu.locked, 'api_nowhp': kanmusu.current_hp, 'api_raisou': [
            kanmusu.stats.torpedo,
            ship.max_stats.torpedo], 'api_lv': kanmusu.level, 'api_slotnum': ship.maxslots, 'api_srate': 1,
    # TODO: Implement stars
        'api_cond': kanmusu.fatigue, 'api_kaihi': [kanmusu.stats.evasion,
            ship.max_stats.evasion], 'api_sortno': ship.number, 'api_fuel': kanmusu.current_fuel, 'api_taiku': [
            kanmusu.stats.antiair, ship.max_stats.antiair], 'api_leng': ship.max_stats.range_, 'api_taisen': [
            kanmusu.stats.antisub, ship.max_stats.antisub], # Guesswork on exp part.
        'api_exp': [kanmusu.experience, LevelHelper.get_exp_required(kanmusu.level, kanmusu.experience),
            0], 'api_slot': equips, 'api_backs': ship.rarity, 'api_sally_area': 0, # dunno
        'api_ndock_item': [0, 0], # TODO
        'api_karyoku': [kanmusu.stats.firepower,
            ship.max_stats.firepower], 'api_maxhp': ship.max_stats.hp, 'api_lucky': [kanmusu.stats.luck,
            ship.max_stats.luck], 'api_ndock_time': 0, 'api_kyouka': [0, 0, 0, 0, 0], 'api_sakuteki': [
            ship.base_stats.los, ship.max_stats.los]
    }
    return kanmusu_data


def fleet(fleet):
    fleet_members = [kanmusu.id for kanmusu in fleet.kanmusu if kanmusu is not None]
    return {
        # Unknown value, always zero for some reason.
        'api_flagship': 0, # The Admiral ID, presumably.
        'api_member_id': g.admiral.id, # The name of the fleet.
        'api_name': fleet.name, # Unknown value, always empty.
        'api_name_id': "", # The local fleet ID.
        'api_id': fleet.number, # List of ships.
        "api_ship": fleet_members + [-1] * (6 - len(fleet_members)), # Mission data?
        "api_mission": [0, 0, 0, 0]
    }


def dock_data(dock_list):
    admiral = g.admiral
    response = []
    count = len(dock_list)
    """ Append admiral dock data """
    for n in range(count):
        dock = dock_list[n]
        response.append({
            'api_member_id': admiral.id, 'api_id': dock.number, 'api_state': 0 if dock.complete is None
            else 2 if dock.complete > time.time()
            else 3 if dock.complete < time.time() else -1, 'api_created_ship_id': dock.kanmusu.ship.id if dock.kanmusu is not None else 0, 'api_complete_time': dock.complete, 'api_complete_time_str': datetime.datetime.fromtimestamp(
                dock.complete / 1000).strftime(
                '%Y-%m-%d %H:%M:%S') if dock.complete is not None else "", 'api_item1': dock.resources.fuel, 'api_item2': dock.resources.ammo, 'api_item3': dock.resources.steel, 'api_item4': dock.resources.baux, 'api_item5': None, })
    """ Fill the rest with empty dock data """
    while count < 4:
        response.append({
            'api_member_id': admiral.id, 'api_id': count + 1, 'api_state': -1, 'api_created_ship_id': 0, 'api_complete_time': 0, 'api_complete_time_str': "", 'api_item1': 0, 'api_item2': 0, 'api_item3': 0, 'api_item4': 0, 'api_item5': 0
        })
        count += 1
    return response


def kdock():
    return dock_data(g.admiral.docks_craft)


def rdock():
    return dock_data(g.admiral.docks_repair)
