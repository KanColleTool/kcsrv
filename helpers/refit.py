from flask import g

from . import member
from db import Kanmusu


def powerup(kanmusu_id,result):
    fleet_data = [member.fleet(fleet) for fleet in g.admiral.fleets]
    api_ship = member.kanmusu(Kanmusu.get(kanmusu_id))
    return {
        "api_powerup_flag": int(result),
        "api_ship": api_ship,
        "api_deck": fleet_data
    }