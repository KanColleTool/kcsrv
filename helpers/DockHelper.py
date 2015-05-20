import random
import datetime
import time

import db
from helpers import ShipHelper
import util


def get_ship_from_recipe(fuel: int=30, ammo: int=30, steel: int=30, baux: int=30) -> int:
    """
    Gets a ship id from the specified recipe.
    :return: The ship id that was chosen.
    """
    ships = db.Recipe.query.filter((db.Recipe.minfuel >= fuel) & (db.Recipe.maxfuel <= fuel)) \
        .filter((db.Recipe.minammo >= ammo) & (db.Recipe.maxammo <= ammo)) \
        .filter((db.Recipe.minsteel >= steel) & (db.Recipe.maxsteel <= steel)) \
        .filter((db.Recipe.minbaux >= baux) & (db.Recipe.maxsteel <= baux))

    ship_choices = [[x.id] * x.chance for x in ships]
    ship_choices = [item for sublist in ship_choices for item in sublist]
    return random.choice(ship_choices)


def update_dock(dock: db.Dock, fuel: int=None, ammo: int=None, steel: int=None, baux: int=None,
                ship: db.AdmiralShip=None, build=True):
    """
    Updates a dock with the correct values.
    Can be called just like ```update_dock(dock)``` to reset the dock.
    :param dock: The dock object to work on.
    :param fuel: The amount of fuel in the recipe.
    :param ammo: The amount of ammo in the recipe.
    :param steel: The amount of steel in the recipe.
    :param baux: The amount of Bauxite in the recipe.
    :param ship: The ship object to add to the dock.
    :return:
    """
    dock.fuel = fuel
    dock.ammo = ammo
    dock.steel = steel
    dock.baux = baux
    if ship is not None:
        dock.cmats = 1
        try:
            if build:
                ntime = util.millisecond_timestamp(
                    datetime.datetime.now() + datetime.timedelta(minutes=ship.ship.buildtime))
            else:
                ntime = util.millisecond_timestamp(
                    datetime.datetime.now() + datetime.timedelta(minutes=ShipHelper.get_repair_time(ship)))
        except TypeError:
            ntime = util.millisecond_timestamp(datetime.datetime.now() + datetime.timedelta(minutes=22))
        dock.complete = ntime
    else:
        dock.cmats = 0
        dock.complete = 0
    dock.ship = ship

    return dock


def get_and_remove_ship(dockid: int, build=True):
    """
    Used by the /getship APIv1 endpoint.

    Retrieves a ship from the specified dock and removes it.
    :param dockid: The specified dock ID.
    :param build: If the ship is being built or not. If false, it's repaired.
    :return: The v1 API data for the dock.
    """
    admiral = util.get_token_admiral_or_error()
    try:
        dock = admiral.docks.all()[dockid]
    except IndexError:
        return None

    dock.fuel, dock.ammo, dock.steel, dock.baux, dock.cmats = 0, 0, 0, 0, 0

    dock.ship.active = True
    if not build:
        dock.ship.current_hp = dock.ship.ship.hp_base if not dock.ship.ship.kai else dock.ship.ship.maxhp
    db.db.session.add(dock.ship)
    api_data = {
        "api_ship_id": dock.ship.ship.id,
        "api_kdock": generate_dock_data(admiral_obj=admiral)['cdock' if build else 'rdock'],
        "api_id": dock.ship.local_ship_num,
        "api_slotitem": [],
        "api_ship": ShipHelper.generate_api_data(admiralid=admiral.id, original_ship=dock.ship)
    }
    dock.ship = None
    dock.complete = None
    db.db.session.add(dock)
    db.db.session.commit()
    return api_data


def craft_ship(fuel: int, ammo: int, steel: int, baux: int, admiral: db.Admiral, dockid: int):
    """
    Crafts a ship from a recipe.
    :param fuel: The amount of fuel to use.
    :param ammo: The amount of ammo to use.
    :param steel: The amount of steel to use.
    :param baux: The amount of bauxite to use.
    :param admiral: The admiral object to use.
    :param dockid: The local dock id.
    :return: The v1 api data for a crafted ship.
    """
    ship = get_ship_from_recipe(fuel, ammo, steel, baux)
    nship = ShipHelper.generate_new_ship(ship, active=False)
    nship.local_ship_num = len(admiral.admiral_ships.all())

    # Change dock data.
    dockid = admiral.docks.all()[dockid]
    dockid = update_dock(dockid, fuel, ammo, steel, baux, nship)
    db.db.session.add(dockid)
    db.db.session.commit()
    admiral.admiral_ships.append(nship)
    db.db.session.add(admiral)
    api_data = {
        "api_ship_id": ship,
        "api_kdock": generate_dock_data(admiral_obj=admiral)['cdock'],
        "api_id": nship.local_ship_num,
        "api_slotitem": [],
        "api_ship": ShipHelper.generate_api_data(admiralid=admiral.id, original_ship=nship)
    }
    db.db.session.commit()
    return api_data


def generate_dock_data(admiral_obj: db.Admiral=None, admiralid: int=None) -> dict:
    """
    Generates v1 dock data.
    :param admiral: Generate from this db.Admiral instance.
    :param admiralid: Generate from this admiral ID.
    :return: A dict containing the dock data. d['rdock'] for repair docks, d['cdock'] for crafting docks
    """
    # TODO: Refactor and make this nicer.
    if admiral_obj:
        admiral = admiral_obj
    elif admiralid:
        admiral = db.Admiral.query.filter_by(id=admiralid)
    ob = {"rdock": [], "cdock": []}
    for x in range(0, 4):
        if admiral.available_cdocks - 1 >= x:
            dock = admiral.docks.all()[x]
            ob['cdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': 0 if dock.complete is None
                                else 2 if dock.complete > time.time()
                                else 3 if dock.complete < time.time() else -1,
                                'api_created_ship_id': dock.ship.ship.id if dock.ship is not None else 0,
                                'api_complete_time': dock.complete,
                                'api_complete_time_str': datetime.datetime.fromtimestamp(
                                    dock.complete / 1000
                                ).strftime('%Y-%m-%d %H:%M:%S') if dock.complete is not None else "",
                                'api_item1': dock.fuel,
                                'api_item2': dock.ammo,
                                'api_item3': dock.steel,
                                'api_item4': dock.baux,
                                'api_item5': dock.cmats
                                })
        else:
            ob['cdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': -1,
                                'api_created_ship_id': 0,
                                'api_complete_time': 0,
                                'api_complete_time_str': "",
                                'api_item1': 0,
                                'api_item2': 0,
                                'api_item3': 0,
                                'api_item4': 0,
                                'api_item5': 0
                                })
    for x in range(4, 8):
        if admiral.available_rdocks - 1 >= x:
            dock = admiral.docks.all()[x]
            ob['rdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': 0 if dock.complete is None
                                else 2 if dock.complete > time.time()
                                else 3 if dock.complete < time.time() else -1,
                                'api_created_ship_id': dock.ship.ship.id if dock.ship is not None else 0,
                                'api_complete_time': dock.complete,
                                'api_complete_time_str': datetime.datetime.fromtimestamp(
                                    dock.complete / 1000
                                ).strftime('%Y-%m-%d %H:%M:%S') if dock.complete is not None else "",
                                'api_item1': dock.fuel,
                                'api_item2': dock.ammo,
                                'api_item3': dock.steel,
                                'api_item4': dock.baux,
                                'api_item5': dock.cmats
                                })
        else:
            ob['rdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': -1,
                                'api_created_ship_id': 0,
                                'api_complete_time': 0,
                                'api_complete_time_str': "",
                                'api_item1': 0,
                                'api_item2': 0,
                                'api_item3': 0,
                                'api_item4': 0,
                                'api_item5': 0
                                })
    return ob
