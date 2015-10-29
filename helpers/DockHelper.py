"""
import random
import datetime
import time

from db import db,Admiral,AdmiralShip,Recipe,Dock
from . import ShipHelper
import util
"""

# from db import db,Dock
import datetime
import random

from flask import g

import util
from db import Recipe, Dock, Kanmusu, db
from . import MemberHelper


def calculate_build_time(kanmusu: Kanmusu):
    # {Total repair time} = {HP loss} * {base repair time} * {ship type} + {30 seconds}
    # Our modified formula: Total = HP Loss * ((Build Time**0.6) + Level)
    return (kanmusu.ship.max_stats.hp - kanmusu.current_hp) * ((kanmusu.ship.buildtime**0.6) + kanmusu.level)


def get_ship_from_recipe(fuel: int=30, ammo: int=30, steel: int=30, baux: int=30) -> int:
    ships = Recipe.query.filter((Recipe.min_resources.fuel >= fuel) & (Recipe.max_resources.fuel <= fuel)) \
        .filter((Recipe.min_resources.ammo >= ammo) & (Recipe.max_resources.ammo <= ammo)) \
        .filter((Recipe.min_resources.steel >= steel) & (Recipe.max_resources.steel <= steel)) \
        .filter((Recipe.min_resources.baux >= baux) & (Recipe.max_resources.baux <= baux))

    ship_choices = [[x.id] * x.chance for x in ships]
    ship_choices = [item for sublist in ship_choices for item in sublist]
    return random.choice(ship_choices)


def update_dock(dock: Dock, fuel: int=None, ammo: int=None, steel: int=None, baux: int=None,
                ship: Kanmusu=None, build=True):
    
    dock.resources.fuel = fuel
    dock.resources.ammo = ammo
    dock.resources.steel = steel
    dock.resources.baux = baux
    if ship is not None:
        try:
            if build:
                ntime = util.millisecond_timestamp(
                    datetime.datetime.now() + datetime.timedelta(minutes=ship.ship.buildtime))
            else:
                ntime = util.millisecond_timestamp(
                    datetime.datetime.now() + datetime.timedelta(minutes=ship.ship.repairtime))
        except TypeError:
            ntime = util.millisecond_timestamp(datetime.datetime.now() + datetime.timedelta(minutes=22))
        dock.complete = ntime
    else:
        dock.complete = 0
    dock.kanmusu = ship

    return dock


def get_and_remove_ship_kdock(dockid: int):
    admiral = g.admiral
    try:
        dock = admiral.docks_craft.all()[dockid]
    except IndexError:
        return None

    dock.resources.fuel, dock.resources.ammo, \
    dock.resources.steel, dock.resources.baux = 0, 0, 0, 0

    dock.kanmusu.active = True

    db.session.add(dock.ship)
    api_data = {
        "api_ship_id": dock.ship.ship.id,
        "api_kdock": MemberHelper.dock_data([dock], False),
        "api_id": dock.kanmusu.number,
        "api_slotitem": [], # TODO: Equipment!
        "api_ship": MemberHelper.kanmusu(kanmusu=dock.kanmusu)
    }
    # Update dock data.
    dock.kanmusu = None
    dock.complete = None
    db.session.add(dock)
    db.session.commit()
    return api_data


def craft_ship(fuel: int, ammo: int, steel: int, baux: int, dockid: int):
    admiral = g.admiral
    ship = get_ship_from_recipe(fuel, ammo, steel, baux)
    nship = Kanmusu().create(ship_api_id=ship)

    # Change dock data.
    dock = admiral.docks_craft.all()[dockid]
    dock = update_dock(dock, fuel, ammo, steel, baux, nship)
    db.db.session.add(dock)
    admiral.add_kanmusu(nship)
    db.db.session.add(admiral)
    api_data = {
        "api_ship_id": ship,
        "api_kdock": MemberHelper.dock_data([dock], False),
        "api_id": nship.local_ship_num,
        "api_slotitem": [],
        "api_ship": MemberHelper.kanmusu(kanmusu=dock.kanmusu)
    }
    db.db.session.commit()
    return api_data

"""
def generate_dock_data(admiral_obj: Admiral=None, admiralid: int=None) -> dict:

    # TODO: Refactor and make this nicer.
    if admiral_obj:
        admiral = admiral_obj
    elif admiralid:
        admiral = Admiral.query.filter_by(id=admiralid)
    else:
        admiral = None
    ob = {"rdock": [], "cdock": []}

    if admiral is None:
        return ob


    #print(admiral.docks.all(), admiral.available_cdocks)

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
        if admiral.available_rdocks - 1 >= x - 3:
            dock = admiral.docks.all()[x]
            ob['rdock'].append({'api_member_id': admiral.id,
                                'api_id': x - 3,
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
                                'api_id': x - 3,
                                'api_state': 0,
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
"""
