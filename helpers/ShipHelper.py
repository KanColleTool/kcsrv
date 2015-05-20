import db
from helpers import LevelHelper
import util

__author__ = 'eyes'

def get_repair_materials(original_ship: db.AdmiralShip):
    """
    Get the amount of materials required to repair a ship.
    :param original_ship: The db.AdmiralShip object that you wish to repair.
    :return: A four part string, "fuel,ammo,steel,bauxite"
    """
    return "0,0,0,0"

def get_repair_time(original_ship: db.AdmiralShip):
    """
    Get the time required to repair a ship
    :param original_ship: The db.AdmiralShip object that you wish to repair
    :return: The time to repair the ship.
    """
    return original_ship.repair_base

def generate_new_ship(shipid: int, fleetid: int=None, active: bool=True) -> db.AdmiralShip:
    """
    Generates a new ship from the specified ship id.
    :param shipid: The ship ID to generate from.
    :param fleetid: The optional fleet ID to give to the ship.
    :return: A new db.AdmiralShip object.
    """
    original_ship = db.Ship.query.filter_by(id=shipid).first()
    assert isinstance(original_ship, db.Ship)
    if not original_ship: return
    admiral_ship = db.AdmiralShip(
        ship = original_ship,
        ammo = original_ship.ammo_max,
        fuel = original_ship.fuel_max,
        exp = 0,
        level = 1,
        repair_base = get_repair_materials(original_ship),
        luck = original_ship.luck_base,
        luck_eq = original_ship.luck_base,
        firepower = original_ship.firepower_base,
        firepower_eq = original_ship.firepower_base,
        armour = original_ship.armour_base,
        torpedo = original_ship.torpedo_base,
        torpedo_eq = original_ship.torpedo_base,
        antiair = original_ship.antiair_base,
        antiair_eq = original_ship.antiair_base,
        antisub = original_ship.antisub_base,
        evasion = original_ship.evasion_base,
        fatigue = 49,
        current_hp = original_ship.hp_base if not original_ship.kai else original_ship.maxhp,
        local_fleet_num=fleetid,
        active=active
    )
    return admiral_ship

def generate_api_data(admiralid: int, local_ship_id: int=None, original_ship: db.AdmiralShip=None) -> dict:
    """
    Generates an APIv1 compatible dictionary to pass to the KanColle official client.
    :param admiralid: The ID of the admiral getting the ship.
    :param local_ship_id:
    :param original_ship:
    :return:
    """
    admiral = db.Admiral.query.filter_by(id=admiralid).first()
    if local_ship_id is not None:
        ship = admiral.admiral_ships.filter_by(local_ship_num=local_ship_id).first()
    elif original_ship:
        ship = original_ship
    else:
        return {}
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
            'api_id': ship.local_ship_num+1,
            'api_karyoku': [ship.firepower_eq, ship.ship.firepower_max],
            'api_maxhp': ship.ship.hp_base if not ship.ship.kai else ship.ship.maxhp,
            'api_lucky': [ship.luck_eq, ship.ship.luck_max],
            'api_ship_id': ship.ship.id,
            'api_ndock_time': 0,
            'api_kyouka': [0, 0, 0, 0, 0],
            'api_sakuteki': [ship.ship.los_base, ship.ship.maxlos]
        }
    return temp_dict