"""
import random
import datetime
import time

from db import db,Admiral,AdmiralShip,Recipe,Dock
from . import ShipHelper
import util
"""
from flask import g
#from db import db,Dock

def dock_data(dock_list):
    admiral = g.admiral
    response = []
    count = len(dock_list)
    """ Append admiral dock data """    
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
                'api_complete_time_str': datetime.datetime.fromtimestamp(
                        dock.complete / 1000
                    ).strftime('%Y-%m-%d %H:%M:%S') if dock.complete is not None else "",
                'api_item1': dock.resources.fuel,
                'api_item2': dock.resources.ammo,
                'api_item3': dock.resources.steel,
                'api_item4': dock.resources.baux,
                'api_item4': 0,
        })
    """ Fill the rest with empty dock data """
    while count < 4:
        response.append({
                'api_member_id': admiral.id,
                'api_id': count+1,
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
        count += 1
    return response


def kdock():
    return dock_data(g.admiral.docks_craft)

def rdock():
    return dock_data(g.admiral.docks_repair)
    
            


"""
def get_ship_from_recipe(fuel: int=30, ammo: int=30, steel: int=30, baux: int=30) -> int:
    ships = Recipe.query.filter((Recipe.minfuel >= fuel) & (Recipe.maxfuel <= fuel)) \
        .filter((Recipe.minammo >= ammo) & (Recipe.maxammo <= ammo)) \
        .filter((Recipe.minsteel >= steel) & (Recipe.maxsteel <= steel)) \
        .filter((Recipe.minbaux >= baux) & (Recipe.maxsteel <= baux))

    ship_choices = [[x.id] * x.chance for x in ships]
    ship_choices = [item for sublist in ship_choices for item in sublist]
    return random.choice(ship_choices)


def update_dock(dock: Dock, fuel: int=None, ammo: int=None, steel: int=None, baux: int=None,
                ship: AdmiralShip=None, build=True):
    
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


def craft_ship(fuel: int, ammo: int, steel: int, baux: int, admiral: Admiral, dockid: int):   
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