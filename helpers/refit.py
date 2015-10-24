from flask import g

from db import Kanmusu


def ship3(kanmusu_id):
    fleet_data = [fleet.fleet() for fleet in g.admiral.fleets]
    return {
        "api_ship_data": [Kanmusu.get(kanmusu_id).kanmusu_data()],
        "api_deck_data": fleet_data,
        "api_slot_data": g.admiral.unsetslot()
    }