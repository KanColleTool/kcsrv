import datetime
import time

from flask import g

from db import db, Equipment, Kanmusu, KanmusuEquipment, AdmiralEquipment
from constants import *


def kanmusu(kanmusu: Kanmusu):
    ship = kanmusu.ship

    # AdmiralShip *must have* entries in AdmiralShipItem table, or we catbomb.
    equips = [equip.admiral_equipment.id if equip.admiral_equipment_id else -1 for equip in kanmusu.equipments]
    modern_stats = kanmusu.modernized_stats
    kanmusu_data = {
        # This must match api_data2 or we get different Ships in the game and DB.
        'api_id': kanmusu.id, 'api_ship_id': ship.api_id,
        'api_onslot': [0, 0, 0, 0, 0],  # ?
        'api_locked_equip': 0,
        'api_bull': kanmusu.current_ammo,
        'api_soukou': [kanmusu.stats.armour, ship.max_stats.armour],
        'api_locked': kanmusu.locked, 'api_nowhp': kanmusu.current_hp,
        'api_raisou': [kanmusu.stats.torpedo, ship.max_stats.torpedo],
        'api_lv': kanmusu.level,
        'api_slotnum': ship.maxslots,
        'api_srate': 1,  # TODO: Implement stars
        'api_cond': kanmusu.fatigue,
        'api_kaihi': [kanmusu.stats.evasion, ship.max_stats.evasion],
        'api_sortno': ship.number,
        'api_fuel': kanmusu.current_fuel,
        'api_taiku': [kanmusu.stats.antiair, ship.max_stats.antiair],
        'api_leng': ship.max_stats.range_,
        'api_taisen': [kanmusu.stats.antisub, ship.max_stats.antisub],  # Guesswork on exp part.
        'api_exp': [kanmusu.experience, kanmusu.get_exp_to_level(), 0],
        'api_slot': equips,
        'api_backs': ship.rarity,
        'api_sally_area': 0,  # dunno
        'api_ndock_item': [0, 0],  # TODO
        'api_karyoku': [kanmusu.stats.firepower, ship.max_stats.firepower],
        'api_maxhp': ship.base_stats.hp,  # Ship "maxhp" is level 100HP, otherwise base is used.
        'api_lucky': [kanmusu.stats.luck, ship.max_stats.luck],
        'api_ndock_time': 0,
        'api_kyouka': [modern_stats.firepower, modern_stats.torpedo, modern_stats.antiair, modern_stats.armour, modern_stats.luck] if modern_stats else [0,0,0,0,0],
        'api_sakuteki': [ship.base_stats.los, ship.max_stats.los]
    }
    return kanmusu_data


def fleet(fleet):
    fleet_members = [kanmusu.id for kanmusu in fleet.kanmusu if kanmusu is not None]
    return {
        # Unknown value, always zero for some reason.
        'api_flagship': 0,
        # The Admiral ID, presumably.
        'api_member_id': g.admiral.id,
        # The name of the fleet.
        'api_name': fleet.name,
        # Unknown value, always empty.
        'api_name_id': "",
        # The local fleet ID.
        'api_id': fleet.number,
        # List of ships.
        "api_ship": fleet_members + [-1] * (6 - len(fleet_members)),
        # Presumably expedition data.
        "api_mission": [0, 0, 0, 0]
    }


def basic():
    """
    Gets the basic info for the admiral.
    :return: A dict containing the KanColle info for the admiral.
    """

    admiral = g.admiral

    return {
        'api_member_id': admiral.id,
        'api_nickname': admiral.user.nickname,
        'api_nickname_id': admiral.user.id,
        'api_active_flag': 1,
        'api_starttime': 1430603452688,
        'api_level': admiral.level,
        'api_rank': admiral.rank,
        'api_experience': admiral.experience,
        'api_fleetname': None,
        'api_comment': "",
        'api_comment_id': "",
        'api_max_chara': admiral.max_kanmusu,
        'api_max_slotitem': admiral.max_equipment,
        'api_max_kagu': admiral.max_furniture,
        'api_playtime': 0,
        'api_tutorial': 0,
        'api_furniture': [1, 1, 1, 1, 1, 1],  # TODO
        'api_count_deck': len(admiral.fleets),
        'api_count_kdock': len(admiral.docks_craft),
        'api_count_ndock': len(admiral.docks_repair),
        'api_fcoin': admiral.furniture_coins,
        'api_st_win': admiral.sortie_successes,
        'api_st_lose': admiral.sortie_total - admiral.sortie_successes,
        'api_ms_count': admiral.expedition_total,
        'api_ms_success': admiral.expedition_successes,
        'api_pt_win': admiral.pvp_successes,
        'api_pt_lose': admiral.pvp_total - admiral.pvp_successes,
        'api_pt_challenged': 0,
        'api_pt_challenged_win': 0,
        # Disables the opening stuff, and skips straight to the game.
        'api_firstflag': int(len(admiral.kanmusu) > 0),  # False means 0
        'api_tutorial_progress': 100,
        'api_pvp': [0, 0]
    }


def dock_data(dock_list, fill=True):
    admiral = g.admiral
    response = []
    count = len(dock_list)
    # Append admiral dock data
    for n in range(count):
        dock = dock_list[n]
        response.append({
            'api_member_id': admiral.id,
            'api_id': dock.number,
            'api_state': 0 if dock.complete is None
            else 2 if dock.complete > time.time()
            else 3 if dock.complete < time.time() else -1,
            'api_created_ship_id': dock.kanmusu.ship.id if dock.kanmusu is not None else 0,
            'api_complete_time': dock.complete,
            'api_complete_time_str': datetime.datetime.fromtimestamp(dock.complete / 1000).strftime('%Y-%m-%d %H:%M:%S')
            if dock.complete is not None else "",
            'api_item1': dock.resources.fuel,
            'api_item2': dock.resources.ammo,
            'api_item3': dock.resources.steel, 'api_item4': dock.resources.baux,
            'api_item5': None})

    # Fill the rest with empty dock data
    if fill:
        while count < 4:
            response.append({
                'api_member_id': admiral.id,
                'api_id': count + 1,
                'api_state': -1,
                'api_created_ship_id': 0,
                'api_complete_time': 0,
                'api_complete_time_str': "",
                'api_item1': 0, 'api_item2': 0, 'api_item3': 0,
                'api_item4': 0, 'api_item5': 0
            })
            count += 1
    return response


def kdock():
    return dock_data(g.admiral.docks_craft)


def rdock():
    return dock_data(g.admiral.docks_repair)


def material():
    admiral = g.admiral
    response = []
    resc = admiral.resources.to_list()
    usables = [NAME_BUCKET, NAME_FLAME, NAME_MATERIAL, NAME_SCREW]
    count = 1
    for value in resc:
        response.append({
            "api_id": count, "api_value": value, "api_member_id": admiral.id
        })
        count += 1
    for usable in usables:
        response.append({
            "api_id": count, "api_value": admiral.get_usable(usable).quantity, "api_member_id": admiral.id
        })
        count += 1
    return response


def slot_info():
    admiral = g.admiral
    return [{
        'api_id': aequip.id, 'api_slotitem_id': aequip.equipment.id, 'api_locked': aequip.locked, 'api_level': aequip.level
    } for aequip in admiral.equipment.join(Equipment).order_by(Equipment.sortno)]


def useitem():
    return [{
        'api_member_id': g.admiral.id, 'api_id': ausable.id, # 'api_value': ausable.quantity,
        'api_usetype': ausable.usable.type_, 'api_category': ausable.usable.category, 'api_name': ausable.usable.name,
    # WHY
        'api_description': [ausable.usable.description,
            ausable.usable.description2], 'api_price': ausable.usable.price, 'api_count': ausable.quantity
    } for ausable in g.admiral.usables]


def unsetslot():
    """
    Listing all not equipped Equips.
    In hindsight, this looks dumb.
    I'm very sure there's a *much* easier way to do this
    """
    admiral = g.admiral

    query_kanmusu = db.session.query(Kanmusu.id).filter(Kanmusu.admiral_id == admiral.id)

    query_equipped = db.session.query(KanmusuEquipment.admiral_equipment_id)\
        .filter(KanmusuEquipment.kanmusu_id.in_(query_kanmusu),
                KanmusuEquipment.admiral_equipment_id != None)

    query = db.session.query(AdmiralEquipment).filter(AdmiralEquipment.admiral_id == admiral.id, \
        ~AdmiralEquipment.id.in_(query_equipped)).join(Equipment).order_by(Equipment.sortno)
    equiplist = query.all()
    response = {}
    response["api_slottype1"] = []
    for equip in equiplist:
        response["api_slottype1"].append(equip.id)
    return response


def ship3(kanmusu_id):
    fleet_data = [fleet(f) for f in g.admiral.fleets]
    return {
        "api_ship_data": [kanmusu(Kanmusu.get(kanmusu_id))],
        "api_deck_data": fleet_data,
        "api_slot_data": unsetslot()
    }