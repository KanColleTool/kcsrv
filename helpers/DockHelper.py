# ID 1 -> 海防艦 -> Costal Defence Ship (?)
# ID 2 -> 駆逐艦 -> Destroyer
# ID 3 -> 軽巡洋艦 -> Light Cruiser
# ID 4 -> 重雷装巡洋艦 -> Torpedo Cruiser
# ID 5 -> 重巡洋艦 -> Heavy Cruiser
# ID 6 -> 航空巡洋艦 -> Aviation Cruiser
# ID 7 -> 軽空母 -> Light Aircraft Carrier
# ID 8 -> 戦艦 -> Battleship
# ID 9 -> Also battleship
# ID 10 -> 航空戦艦 -> Aviation battleship
# ID 11 -> 正規空母 -> Aircraft carrier
# ID 12 -> 超弩級戦艦 -> Super Dreadnought
# ID 13 -> 潜水艦 -> Submarine
# ID 14 -> 潜水空母 -> Submarine Aircraft Carrier
# ID 15 -> 補給艦 -> Supply Vessel/Replenishment Oiler?
# ID 16 -> 水上機母艦 -> Seaplane Carrier
# ID 17 -> 揚陸艦 -> amphibious assault ship
# ID 18 -> 装甲空母 -> Armored aircraft carrier
# ID 19 -> 工作艦 -> Work Ship
# ID 20 -> 潜水母艦 -> Submarine Tender
# ID 21 -> 練習巡洋艦 -> Practice Cruiser
# from db import db,Dock
import random

from flask import abort
from flask import g
from sqlalchemy import text

from db import Kanmusu, db, Ship
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
        dock = admiral.docks_craft[dockid]
    except IndexError:
        abort(404)
        return None

    if dock.kanmusu is None:
        # ....
        abort(400)
        return

    dock.kanmusu.active = True

    api_data = {
        "api_ship_id": dock.kanmusu.ship.api_id,
        "api_kdock": MemberHelper.dock_data([dock], False),
        "api_id": dock.kanmusu.number,
        "api_slotitem": [], # TODO: Equipment!
        "api_ship": MemberHelper.kanmusu(kanmusu=dock.kanmusu)
    }
    # Update dock data.
    db.session.add(dock.kanmusu)
    dock.update(None)
    db.session.add(dock)
    db.session.commit()
    return api_data


def craft_ship(fuel: int, ammo: int, steel: int, baux: int, dockid: int):
    admiral = g.admiral
    ship = get_ship_from_recipe(fuel, ammo, steel, baux)
    if ship:
        nship = Kanmusu(ship)
        nship.number = len(g.admiral.kanmusu)
    else:
        print("Something bad happened. Where are your recipes?")
        abort(404)
        return

    # Change dock data.
    try:
        dock = admiral.docks_craft[dockid]
    except IndexError:
        abort(404)
        return

    if dock.kanmusu is not None:
        # wat
        abort(400)
        return

    dock = dock.update(nship, fuel, ammo, steel, baux, True)

    admiral.resources.sub(fuel, ammo, steel, baux)

    db.session.add(dock)
    admiral.add_kanmusu(nship)
    db.session.add(admiral)
    api_data = {
        "api_ship_id": nship.ship.api_id,
        "api_kdock": MemberHelper.dock_data([dock], False),
        "api_id": nship.number,
        "api_slotitem": [],
        "api_ship": MemberHelper.kanmusu(kanmusu=dock.kanmusu)
    }
    db.session.commit()
    return api_data
