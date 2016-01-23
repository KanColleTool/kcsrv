"""Expedition blueprint."""
import datetime

from flask import Blueprint, g
from flask import request, abort
import time

import util
from db import Expedition, Fleet, Admiral, db
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
