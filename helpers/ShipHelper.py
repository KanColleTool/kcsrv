from db import db,Admiral,AdmiralShip,Ship,AdmiralShipItem,AdmiralItem,Fleet
from helpers import LevelHelper
import util


def get_repair_materials(original_ship: AdmiralShip):
    """
    Get the amount of materials required to repair a ship.
    :param original_ship: The AdmiralShip object that you wish to repair.
    :return: A four part string, "fuel,ammo,steel,bauxite"
    """
    return "0,0,0,0"

def get_repair_time(original_ship: AdmiralShip):
    """
    Get the time required to repair a ship
    :param original_ship: The AdmiralShip object that you wish to repair
    :return: The time to repair the ship.
    """
    return original_ship.repair_base

def generate_new_ship(shipid: int, fleetid: int=None, active: bool=True):
    """
    Generates a new ship from the specified ship id.
    :param shipid: The ship ID to generate from.
    :param fleetid: The optional fleet ID to give to the ship.
    :return: A new AdmiralShip object.
    """
    original_ship = Ship.query.filter_by(id=shipid).first()
    assert isinstance(original_ship, Ship)
    if not original_ship: return
    admiral_ship = AdmiralShip(
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

def generate_api_data(admiralid: int, local_ship_id: int=None, original_ship: AdmiralShip=None):
    """"
    Use get_admiral_ship_api_data instead.
    """
    """
    Generates an APIv1 compatible dictionary to pass to the KanColle official client.
    :param admiralid: The ID of the admiral getting the ship.
    :param local_ship_id:
    :param original_ship:
    :return:
    """
    admiral = Admiral.query.filter_by(id=admiralid).first()
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

def assign_ship(admiral: Admiral, ship_id: int):
    ship = generate_new_ship(ship_id, 0)
    # Assign ship the correct local ship number.
    ship.local_ship_num = len(admiral.admiral_ships.all())
    for n in range(ship.ship.maxslots):
        db.session.add(AdmiralShipItem(slot=n,admiral_ship=ship))
    # Create a new fleet.
    fleet = Fleet()
    # Add the ship to the first fleet.
    fleet.ships.append(ship)
    # Add the ship to the admiral
    admiral.admiral_ships.append(ship)
    # Add the fleet to the admiral
    admiral.fleets.append(fleet)
    db.session.add(admiral)

def change_ship_item(admiral_ship_id,admiral_item_id,slot):
    #TODO: When remove gear, reorder slots to keep top slots filled.
    admiral_item_id = None if int(admiral_item_id) == -1 else admiral_item_id
    query = db.session.query(AdmiralShipItem)\
    .filter(AdmiralShipItem.admiral_ship_id==admiral_ship_id,AdmiralShipItem.slot==slot)\
    .update({"admiral_item_id":admiral_item_id})
    db.session.commit()

def get_admiral_ship_api_data(admiral_ship_id):
    # I mostly copied this from ShipHelper.generate_api_data
    admiral_ship = db.session.query(AdmiralShip).get(admiral_ship_id)
    ship = admiral_ship.ship

    # AdmiralShip *must have* entries in AdmiralShipItem table, or we catbomb.
    # Currently this is done manually. (Fixing it asap)
    items = [item.admiral_item_id if item.admiral_item_id else -1 for item in admiral_ship.items]
    
    api_ship_data = {
            'api_id': admiral_ship.id,
            'api_onslot': [0, 0, 0, 0, 0], #?
            'api_locked_equip': 0,
            'api_bull': admiral_ship.ammo,
            'api_soukou': [admiral_ship.armour, ship.armour_max],
            'api_locked': admiral_ship.heartlocked,
            'api_nowhp': admiral_ship.current_hp,
            'api_raisou': [admiral_ship.torpedo_eq, ship.torpedo_max],
            'api_lv': admiral_ship.level,
            'api_slotnum': ship.maxslots,
            'api_srate': 1,  # TODO: Implement stars
            'api_cond': admiral_ship.fatigue,
            'api_kaihi': [admiral_ship.evasion, ship.evasion_max],
            'api_sortno': ship.number,
            'api_fuel': admiral_ship.fuel,
            'api_taiku': [admiral_ship.antiair_eq, ship.antiair_max],
            'api_leng': ship.srange,
            'api_taisen': [admiral_ship.antisub, ship.antisub_base],
            # Guesswork on exp part.
            'api_exp': [admiral_ship.exp, LevelHelper.get_exp_required(admiral_ship.level, admiral_ship.exp), 0],
            #'api_slot': items,
            'api_slot': items,
            'api_backs': ship.rarity,
            'api_sally_area': 0,  # dunno
            'api_ndock_item': list(map(int, util.take_items(admiral_ship.repair_base.split(','), [1, 3]))),
            'api_id': admiral_ship.id,
            'api_karyoku': [admiral_ship.firepower_eq, ship.firepower_max],
            'api_maxhp': ship.hp_base if not ship.kai else ship.maxhp,
            'api_lucky': [admiral_ship.luck_eq, ship.luck_max],
            'api_ship_id': ship.id,
            'api_ndock_time': 0,
            'api_kyouka': [0, 0, 0, 0, 0],
            'api_sakuteki': [ship.los_base, ship.maxlos]
    }
    return api_ship_data

def assign_fleet(admiral_ship,fleet,position):
    query = db.session.query(FleetShip).filter(FleetShip.fleet_id==fleet.id,FleetShip.position==position)
    print(query)
    print(fleet.id)
    print(position)
    fleet_ship = query.first()

    fleet_ship.ship = admiral_ship
    db.session.add(fleet_ship)
    db.session.commit()