from flask import g

import util
from constants import *
from db import db, Equipment, Kanmusu, KanmusuEquipment, AdmiralEquipment
from . import data


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

def kdock():
    return data.kdock()

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


def port():
    admiral = g.admiral
    response = {}
    # TODO: Log entry
    response['api_log'] = [{
        "api_state": "0", "api_no": 0, "api_type": "1", "api_message": "ayy lmao"
    }]
    # Background music?
    response["api_p_bgm_id"] = 100
    # This sets the parallel quest count. Don't know what higher values do, default is 5.
    # I set it to ten because fuck the police
    response["api_parallel_quest_count"] = 10
    # Combined flag? Event data probably.
    response["api_combined_flag"] = 0
    # API basic - a replica of api_get_member/basic
    response['api_basic'] = util.merge_two_dicts(basic(), {
        'api_medals': 0, 'api_large_dock': 0
    })
    # Fleets.
    response['api_deck_port'] = [data.fleet(fleet) for fleet in admiral.fleets]
    # Materials.
    materials = []
    resc = admiral.resources.to_list()
    usables = [NAME_BUCKET, NAME_FLAME, NAME_MATERIAL, NAME_SCREW]
    count = 1
    for value in resc:
        materials.append({
            "api_id": count, "api_value": value, "api_member_id": admiral.id
        })
        count += 1
    for usable in usables:
        materials.append({
            "api_id": count, "api_value": admiral.get_usable(usable).quantity, "api_member_id": admiral.id
        })
        count += 1
    response['api_material'] = materials

    response['api_ship'] = [data.kanmusu(kanmusu) for kanmusu in admiral.kanmusu if kanmusu.active]

    # Generate ndock.
    response['api_ndock'] = data.rdock()
    return response
