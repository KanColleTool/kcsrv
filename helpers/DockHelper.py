# from db import db,Dock
import random

from flask import abort
from flask import g
from sqlalchemy import text

from db import Kanmusu, db
from . import MemberHelper


def calculate_repair_time(kanmusu: Kanmusu):
    # {Total repair time} = {HP loss} * {base repair time} * {ship type} + {30 seconds}
    # Our modified formula: Total = HP Loss * ((Build Time**0.6) + Level)
    return (kanmusu.ship.max_stats.hp - kanmusu.current_hp) * ((kanmusu.ship.buildtime**0.6) + kanmusu.level)


def get_ship_from_recipe(fuel: int=30, ammo: int=30, steel: int=30, baux: int=30) -> int:

    ship_t = text("""select ship_id, chance from recipe
      join recipe__resources min on recipe.min_resources_id = min.id
      join recipe__resources max on recipe.max_resources_id = max.id
      where
      :fuel between min.fuel and max.fuel and
      :ammo between min.ammo and max.ammo and
      :steel between min.steel and max.steel and
      :baux between min.baux and max.baux;
    """)

    ships = db.session.execute(ship_t, {"fuel": fuel, "ammo": ammo, "steel": steel, "baux": baux})

    if not ships:
        return None

    ship_choices = [[x[0]] * x[1] for x in ships]
    ship_choices = [item for sublist in ship_choices for item in sublist]
    return random.choice(ship_choices)


def get_and_remove_ship_kdock(dockid: int):
    admiral = g.admiral
    try:
        dock = admiral.docks_craft.all()[dockid]
    except IndexError:
        abort(404)
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
    print("ship is", ship)
    if ship:
        nship = Kanmusu(ship)
        nship.number = len(g.admiral.kanmusu)
    else:
        print("Something bad happened. Where are your recipes?")
        abort(404)
        return

    print("nship is", nship)

    # Change dock data.
    try:
        dock = admiral.docks_craft[dockid]
    except IndexError:
        abort(404)
        return

    dock = dock.update(fuel, ammo, steel, baux, nship, True)

    admiral.resources.sub(fuel, ammo, steel, baux)

    db.session.add(dock)
    admiral.add_kanmusu(nship)
    db.session.add(admiral)
    api_data = {
        "api_ship_id": ship,
        "api_kdock": MemberHelper.dock_data([dock], False),
        "api_id": nship.number,
        "api_slotitem": [],
        "api_ship": MemberHelper.kanmusu(kanmusu=dock.kanmusu)
    }
    db.session.commit()
    return api_data
