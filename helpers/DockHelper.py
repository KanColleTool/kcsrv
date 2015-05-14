import random
import datetime

import db
from helpers import ShipHelper
import util


def get_ship_from_recipe(fuel=30, ammo=30, steel=30, baux=30):
    admiral = util.get_token_admiral_or_error()
    if admiral.user.nickname == "upfinnarn":
        # Naka-chan is shit.
        return 56
    ships = db.Recipe.query.filter((db.Recipe.minfuel >= fuel) & (db.Recipe.maxfuel <= fuel)) \
        .filter((db.Recipe.minammo >= ammo) & (db.Recipe.maxammo <= ammo)) \
        .filter((db.Recipe.minsteel >= steel) & (db.Recipe.maxsteel <= steel)) \
        .filter((db.Recipe.minbaux >= baux) & (db.Recipe.maxsteel <= baux))

    ship_choices = [x.id * x.chance for x in ships]
    return random.choice(ship_choices)


def update_dock(dock: db.Dock, fuel: int, ammo: int, steel: int, baux: int, ship: db.AdmiralShip):
    dock.fuel = fuel
    dock.ammo = ammo
    dock.steel = steel
    dock.baux = baux
    dock.cmats = 1

    dock.ship = ship

    ntime = util.millisecond_timestamp(datetime.datetime.now() + datetime.timedelta(minutes=ship.ship.buildtime))
    dock.complete = ntime
    return dock


def craft_ship(fuel: int, ammo: int, steel: int, baux: int, admiral: db.Admiral, dock: int):
    ship = get_ship_from_recipe(fuel, ammo, steel, baux)
    nship = ShipHelper.generate_new_ship(ship, active=False)
    nship.local_ship_num = len(admiral.admiral_ships.all())

    # Change dock data.
    dock = admiral.crafting_docks.all()[dock]
    dock = update_dock(dock, fuel, ammo, steel, baux, nship)
    db.db.session.add(dock)
    db.db.session.commit()
    admiral.admiral_ships.append(nship)
    db.db.session.add(admiral)
    api_data = {
        "api_ship_id": ship,
        "api_kdock": generate_dock_data(admiral),
        "api_id": nship.local_ship_num,
        "api_slotitem": [],
        "api_ship": ShipHelper.generate_api_data(admiralid=admiral.id, original_ship=nship)
    }
    db.db.session.commit()
    return api_data


def generate_dock_data(admiral_obj: db.Admiral=None, admiralid: int=None) -> dict:
    """
    Generates dock data.
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
            dock = admiral.crafting_docks.all()[x]
            ob['cdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': dock.state,
                                'api_created_ship_id': dock.ship.ship.id if dock.ship is not None else 0,
                                'api_complete_time': dock.complete,
                                'api_complete_time_str': datetime.datetime.fromtimestamp(
                                    dock.complete/1000
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
    for x in range(0, 4):
        if admiral.available_rdocks - 1 >= x:
            dock = admiral.repair_docks.all()[x]
            ob['rdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': dock.state,
                                'api_created_ship_id':dock.ship.ship.id if dock.ship is not None else 0,
                                'api_complete_time': dock.complete,
                                'api_complete_time_str': datetime.datetime.fromtimestamp(
                                    dock.complete/1000
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
