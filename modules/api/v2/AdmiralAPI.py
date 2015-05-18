# If you're gonna yell at me going "oh SunDwarf you haven't even got the official game API implemented yet aeee"
# Please save your breath
# I have most of the basics implemented, the rest to implement are just things like repairs, sorties, quests, etc
# Which I really don't want to have to do right now, for unspecified emotional reasons.

import json

from flask import Blueprint

import util

admiral_api_v2 = Blueprint("admiral_api_v2", __name__)


@admiral_api_v2.route("/<token>")
def base_token(token):
    admiral = util.get_admiral_v2_from_id(token)
    if not admiral:
        return "Invalid API token/ID", 404
    else:
        return admiral.user.nickname


@admiral_api_v2.route("/<token>/userinfo")
def get_userinfo(token):
    admiral = util.get_admiral_v2_from_id(token)
    if not admiral:
        return "Invalid API token/ID", 404
    tdict = {
        "id": admiral.id,
        "name": admiral.user.nickname,
        "level": admiral.level,
        "experience": admiral.experience,
        "maxships": admiral.max_ships,
        "maxitems": admiral.max_equips,
        "tutorial_completed": admiral.setup,
        "fleets_available": admiral.available_fleets,
        "maxquests": 5,  # Temporary
        "cdocks_available": admiral.available_cdocks,
        "rdocks_available": admiral.available_rdocks
    }
    return json.dumps(tdict), 200, {"Content-Type": "application/json"}


@admiral_api_v2.route("/<token>/material/<matid>")
def material(token, matid):
    matid = int(matid) if matid != "all" else matid
    admiral = util.get_admiral_v2_from_id(token)
    resources = admiral.resources.split(',')
    if matid == "all":
        return json.dumps(
            {"materials": [{"id": num, "count": int(count)} for num, count in enumerate(resources)]}
        ), 200, {"Content-Type": "application/json"}
    else:
        if len(resources) < matid:
            return "Invalid resource ID", 400
        else:
            return json.dumps(
                {"materials": [{"id": matid, "count": int(resources[matid])}]}
            ), 200, {"Content-Type": "application/json"}
