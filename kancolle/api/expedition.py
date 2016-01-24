"""Expedition blueprint."""
import datetime
from flask import Blueprint, g
from flask import request, abort
import time

from sqlalchemy_utils import InstrumentedList

import util
from app import logger
from db import Expedition, Fleet, Admiral, db
from helpers import MemberHelper
from util import prepare_api_blueprint, svdata

api_mission = Blueprint("api_mission", __name__)
prepare_api_blueprint(api_mission)


@api_mission.route("/start", methods=["GET", "POST"])
def start_mission():
    # This is mostly an internal method.
    # This sets up the fleet for an expedition, sending them out.

    # First, get the required data from the request.
    fleet_id = int(request.values.get("api_deck_id")) - 1
    expedition_id = int(request.values.get("api_mission_id"))
    # There's an extra value, api_mission.
    # No idea what it does.

    # Also, api_serial_cid
    # This is presumably an anti-bot method by DMM.
    # We don't have these, because we don't have the game source code (and never will)
    # So we ignore this

    # Get the expedition requested by the ID.
    expedition = Expedition.query.filter(Expedition.id == expedition_id).first_or_404()

    # Get the fleet requested by the ID.
    try:
        fleet = g.admiral.fleets[fleet_id]
    except IndexError:
        abort(404)
        return

    # Set the fleet up.
    if fleet.expedition is not None:
        # Nice try.
        abort(400)
        return

    # Set the expedition && time.
    fleet.expedition = expedition
    fleet.expedition_completed = time.time() + expedition.time_taken

    db.session.add(fleet)
    db.session.commit()

    # Internal state updated, now to reflect this state on the rest of the app.
    return svdata(
        {"api_complatetime": util.
            millisecond_timestamp(datetime.datetime.now() + datetime.timedelta(seconds=expedition.time_taken)),
         "api_complatetime_str": datetime.datetime.fromtimestamp(fleet.expedition_completed / 1000)
            .strftime('%Y-%m-%d %H:%M:%S')
         })


@api_mission.route('/result', methods=["GET", "POST"])
def expd_result():
    # Horrible bastard code to get the result of the expedition.
    fleet_id = int(request.values.get("api_deck_id")) - 1

    try:
        fleet = g.admiral.fleets[fleet_id]
    except IndexError:
        logger.warn("Fleet does not exist -> {}".format(fleet_id))
        abort(404)
        return

    if not fleet.expedition:
        logger.warn("Fleet not on expedition -> {}".format(fleet))
        abort(400)
        return

    # Similar to the official servers, we calculate everything in expd_result
    # instead of calculating everything in mission. Meaning nobody knows the result of the expedition until this
    # method is called and it's all calculated.

    # Check the timings.
    if fleet.expedition_completed >= time.time() and not fleet.expedition_cancelled:
        logger.warn("Expedition_Completed ({}) >= Current Time ({})".format(fleet.expedition_completed, time.time()))
        # Don't cheat.
        abort(400)
        return

    # What did the fleet look like again?
    res = fleet.expedition.constraints
    assert isinstance(res, dict)

    # Check in order.
    hq_level_min = res.get("hq_level_min", 0)
    required_ships = res.get("required_ships", {})

    # Enter the world's hackiest solution.
    def check_requirements():
        # This inline-function allows us to check the requirements then exit if needed.

        # First, check HQ level.
        if hq_level_min > g.admiral.level:
            return False
        # Next, check ships.
        else:
            min_ships_total = required_ships.get("min_ships_total", 1)
            if len(fleet.kanmusu) < min_ships_total:
                return False
            ship_types = {}
            for kanmusu in fleet.kanmusu:
                if kanmusu.ship.type_ not in ship_types:
                    ship_types[kanmusu.ship.type_] = 0
                ship_types[kanmusu.ship.type_] += 1
            # Check expedition restrictions
            types = required_ships.get("ship_types", {})
            for t, amount in types.items():
                if ship_types.get(t, 0) < amount:
                    return False
        return True

    if not fleet.expedition_cancelled:
        met_requirements = check_requirements()
    else:
        met_requirements = False

    # Update internal state.
    g.admiral.expedition_total += 1
    g.admiral.expeditions.append(fleet.expedition)
    if met_requirements:
        g.admiral.expedition_successes += 1
        g.admiral.experience += 30
        g.admiral.fix_level()

        api_exp_get = []

        # Level up the kanmusus.
        for kanmusu in fleet.kanmusu:
            # Expeditions are not a good way of levelling up
            kanmusu.experience += (kanmusu.level * 3)
            api_exp_get.append(kanmusu.level * 3)
            kanmusu.fix_level()
            db.session.add(kanmusu)

        # Update resources.
        g.admiral.resources.add(*fleet.expedition.resources_granted.to_list())
    else:
        g.admiral.experience += 5
        g.admiral.fix_level()

        api_exp_get = [0 for _ in fleet.kanmusu]

    data = {
        "api_ship_id": [-1] + [kanmusu.number for kanmusu in fleet.kanmusu],
        "api_clear_result": int(met_requirements),
        "api_get_exp": 30 if met_requirements else 5 if not fleet.expedition_cancelled else 0,
        "api_member_lv": g.admiral.level,
        "api_member_exp": g.admiral.experience,
        "api_get_ship_exp": api_exp_get,
        "api_get_exp_lvup": [[kanmusu.experience, kanmusu.experience + kanmusu.get_exp_to_level()] for kanmusu in
                             fleet.kanmusu],
        "api_maparea_name": "???",
        "api_detail": "???",
        "api_quest_name": "Expedition {}".format(fleet.expedition.id),
        "api_quest_level": 1,
        "api_get_material": fleet.expedition.resources_granted.to_list() if met_requirements else -1,
        "api_useitem_flag": [
            0,
            0
        ]
    }
    fleet.expedition = None
    fleet.expedition_completed = None
    fleet.expedition_cancelled = None
    db.session.add(fleet)
    db.session.add(g.admiral)
    db.session.commit()
    sv = svdata(data)
    return sv


@api_mission.route("/return_instruction", methods=["GET", "POST"])
def cancel():
    """Cancels a mission"""
    fleet_id = int(request.values.get("api_deck_id")) - 1

    try:
        fleet = g.admiral.fleets[fleet_id]
    except IndexError:
        logger.warn("Fleet does not exist -> {}".format(fleet_id))
        abort(404)
        return

    fleet.expedition_cancelled = True
    db.session.add(fleet)
    db.session.commit()
    return svdata(MemberHelper.expedition(fleet, cancelled=True))
