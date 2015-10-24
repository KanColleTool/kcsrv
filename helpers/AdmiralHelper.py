import util
# from db import db,User,Admiral,Dock,AdmiralQuest,Resource,AdmiralItem
from . import DockHelper
from constants import *
from db import db, Equipment, Kanmusu, KanmusuEquipment, AdmiralEquipment
from flask import g


"""These are API version 1 functions only."""


def basic():
    admiral = g.admiral
    """
    Gets the basic info for the admiral.
    :return: A dict containing the KanColle info for the admiral.
    """
    return {
        'api_member_id': admiral.id, 'api_nickname': admiral.user.nickname, 'api_nickname_id': admiral.user.id, 'api_active_flag': 1, 'api_starttime': 1430603452688, 'api_level': admiral.level, 'api_rank': admiral.rank, 'api_experience': admiral.experience, 'api_fleetname': None, 'api_comment': "", 'api_comment_id': "", 'api_max_chara': admiral.max_kanmusu, 'api_max_slotitem': admiral.max_equipment, 'api_max_kagu': admiral.max_furniture, 'api_playtime': 0, 'api_tutorial': 0, 'api_furniture': [
            1, 1, 1, 1, 1, 1], # TODO
        'api_count_deck': len(admiral.fleets), 'api_count_kdock': len(admiral.docks_craft), 'api_count_ndock': len(
            admiral.docks_repair), 'api_fcoin': admiral.furniture_coins, 'api_st_win': admiral.sortie_successes, 'api_st_lose': admiral.sortie_total - admiral.sortie_successes, 'api_ms_count': admiral.expedition_total, 'api_ms_success': admiral.expedition_successes, 'api_pt_win': admiral.pvp_successes, 'api_pt_lose': admiral.pvp_total - admiral.pvp_successes, 'api_pt_challenged': 0, 'api_pt_challenged_win': 0,
        # Disables the opening stuff, and skips straight to the game.
        'api_firstflag': 1 if len(admiral.kanmusu) == 0 else 0, # meh.
        'api_tutorial_progress': 100, 'api_pvp': [0, 0]
    }


def slot_info():
    admiral = g.admiral
    return [{
        'api_id': aequip.id, 'api_slotitem_id': aequip.equipment.id, 'api_locked': aequip.locked, 'api_level': aequip.level
    } for aequip in admiral.equipment.join(Equipment).order_by(Equipment.sortno)]


def useitem():
    return [{
        'api_member_id': g.admiral.id, 'api_id': ausable.id, # 'api_value': ausable.quantity,
        'api_usetype': ausable.usables.type_, 'api_category': ausable.usables.category, 'api_name': ausable.usables.name,
    # WHY
        'api_description': [ausable.usables.description,
            ausable.usables.description2], 'api_price': ausable.usables.price, 'api_count': ausable.quantity
    } for ausable in g.admiral.usables]


def unsetslot():
    """
    Listing all not equipped Equips.
    In hindsight, this looks dumb.
    I'm very sure there's a *much* easier way to do this    
    """
    admiral = g.admiral

    query_kanmusu = db.session.query(Kanmusu.id).filter(Kanmusu.admiral_id == admiral.id)

    query_equipped = db.session.query(KanmusuEquipment.admiral_equipment_id).filter(
        KanmusuEquipment.kanmusu_id.in_(query_kanmusu), KanmusuEquipment.admiral_equipment_id != None)

    query = db.session.query(AdmiralEquipment).filter(AdmiralEquipment.admiral_id == admiral.id, \
        ~AdmiralEquipment.id.in_(query_equipped)).join(Equipment).order_by(Equipment.sortno)
    itemlist = query.all()

    response = {}
    response["api_slottype1"] = []
    for admiral_item, item in itemlist:
        response["api_slottype1"].append(admiral_item.id)
    return response


def port():
    admiral = g.admiral
    response = {"api_data": {}}
    # TODO: Log entry
    response["api_data"]['api_log'] = [{
        "api_state": "0", "api_no": 0, "api_type": "1", "api_message": "ayy lmao"
    }]
    # Background music?
    response["api_data"]["api_p_bgm_id"] = 100
    # This sets the parallel quest count. Don't know what higher values do, default is 5.
    # I set it to ten because fuck the police
    response["api_data"]["api_parallel_quest_count"] = 10
    # Combined flag? Event data probably.
    response["api_data"]["api_combined_flag"] = 0
    # API basic - a replica of api_get_member/basic
    response['api_data']['api_basic'] = util.merge_two_dicts(basic(), {
        'api_medals': 0, 'api_large_dock': 0
    })
    response['api_data']['api_deck_port'] = []
    # Fleets.
    for fleet in admiral.fleets:
        fleet_members = [kanmusu.number + 1 for kanmusu in fleet.kanmusu if kanmusu is not None]
        temp_dict = {
            # Unknown value, always zero for some reason.
            'api_flagship': 0, # The Admiral ID, presumably.
            'api_member_id': admiral.id, # The name of the fleet.
            'api_name': fleet.name, # Unknown value, always empty.
            'api_name_id': "", # The local fleet ID.
            'api_id': fleet.number, # List of ships.
            "api_ship": fleet_members + [-1] * (6 - len(fleet_members)), # Mission data?
            "api_mission": [0, 0, 0, 0]
        }
        response['api_data']['api_deck_port'].append(temp_dict)

    # Materials.
    materials = admiral.resources.to_list()
    materials.append(admiral.get_usables(NAME_BUCKET).quantity)
    materials.append(admiral.get_usables(NAME_FLAME).quantity)
    materials.append(admiral.get_usables(NAME_MATERIAL).quantity)
    materials.append(admiral.get_usables(NAME_SCREW).quantity)
    response['api_data']['api_material'] = materials

    response['api_data']['api_ship'] = [ShipHelper.kanmusu_data(kanmusu) for kanmusu in admiral.kanmusu if
        kanmusu.active]

    # Generate ndock.
    response['api_data']['api_ndock'] = DockHelper.rdock()
    return response


"""
def get_admiral_furniture():
    return [int(x) for x in util.get_token_admiral_or_error().furniture.split(',')]

def get_admiral_sorties():
    
    Gets Admiral's unlocked Sorties
    :return: A list containing dicts of KanColle Sortie info for the Admiral
    
    admiral = util.get_token_admiral_or_error()
    data = []
    for admiral_sortie in admiral.sorties.all():
        sortie = db.Sortie.query.filter_by(id=admiral_sortie.sortie_id).first()
        data.append({
            'api_id': sortie.level,
            'api_cleared': admiral_sortie.cleared,
            'api_exboss_flag': sortie.is_boss,
            'api_defeat_count': admiral_sortie.defeat_count #Unnecessary if is not boss
        })
    return data

def get_admiral_v2(api_token: str):    
    user = User.query.filter_by(api_token=api_token).first()
    if not user:
        return None
    if not user.admiral:
        adm = db.Admiral()
        user.admiral = adm
        db.session.add(user)
        db.session.commit()
    return user.admiral

def get_admiral_v2_from_id_or_token(search: object):

    if len(search) == 40:
        user = User.query.filter_by(api_token=search).first()
    elif search:
        user = User.query.filter_by(id=search).first()
    else:
        return None
    if not user:
        return None
    if not user.admiral:
        adm = db.Admiral()
        user.admiral = adm
        db.session.add(user)
        db.session.commit()
    return user.admiral

def activate_quest(quest_id,admiral=None,admiral_id=None):
    admiral = admiral if admiral else Admiral.query.get(admiral_id)
    AdmiralQuest.query.filter_by(admiral_id=admiral.id,quest_id=quest_id).update({"state":2})
    db.session.commit()

def deactivate_quest(quest_id,admiral=None,admiral_id=None):
    admiral = admiral if admiral else Admiral.query.get(admiral_id)
    AdmiralQuest.query.filter_by(admiral_id=admiral.id,quest_id=quest_id).update({"state":1})
    db.session.commit()

def get_admiral_deck_api_data(admiral):
    count = 0
    # Fleets.    
    fleet_api_data = []
    for fleet in admiral.fleets.all():
        count += 1
        ships = [ship.local_ship_num+1 for ship in fleet.ships.all() if ship is not None]
        fleet_api_data.append({
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
        })
    return fleet_api_data

def get_admiral_resources_api_data(admiral):
    resources = admiral.resources.to_list()
    data = [{
        "api_id": n + 1,
        "api_member_id": admiral.id,
        "api_value": resource
    } for n,resource in enumerate(resources)]
    # I have no idea what this is, it can have any api_value
    # but without it flame/bucket/mat always show up as 0.
    data.append({"api_id": 8,"api_member_id": admiral.id,"api_value":1})
    return data


def admiral_grant_resources(admiral,resource=None,**kwargs):
    admiral.resources = ResourceHelper.update_resource(admiral.resources,resource,kwargs)
    db.session.add(admiral)
    db.session.commit()

def admiral_grant_item(admiral,item_id,quantity=1):
    for _ in range(quantity):
        db.session.add(AdmiralItem(admiral_id=admiral.id,item_id=item_id))
    db.session.commit()

def admiral_grant_ship(admiral,ship_id=None,ship_api_id=None,quantity=1):
    for _ in range(quantity):
        admiral.admiral_ships.append(ShipHelper.get_new_admiral_ship(admiral,ship_id,ship_api_id))
    db.session.add(admiral)
    db.session.commit()
"""
