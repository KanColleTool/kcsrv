from flask import g
from . import data,gamestart
from db import Kanmusu

def ship3(kanmusu_id):
    fleet_data = [data.fleet(fleet) for fleet in g.admiral.fleets]
    return {
        "api_ship_data": [data.kanmusu(Kanmusu.get(kanmusu_id))],
        "api_deck_data": fleet_data,
        "api_slot_data": gamestart.unsetslot()
    }

def powerup(kanmusu_id,result):
    fleet_data = [data.fleet(fleet) for fleet in g.admiral.fleets]
    api_ship = data.kanmusu(Kanmusu.get(kanmusu_id))
    return {
        "api_powerup_flag": int(result),
        "api_ship": api_ship,
        "api_deck": fleet_data
    }

def material():
    return data.material()