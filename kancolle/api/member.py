from collections import OrderedDict
from flask import request, g, Blueprint, redirect, url_for
from db import Kanmusu, Admiral, Expedition
from helpers import MemberHelper
from helpers.MemberHelper import fleet
from util import svdata
from constants import HQ_LEVEL

api_member = Blueprint("api_game", __name__)


@api_member.route('/basic', methods=['GET', 'POST'])
def basic():
    """Basic admiral data."""
    return svdata(MemberHelper.basic())


@api_member.route('/furniture', methods=['GET', 'POST'])
def furniture():
    """Available furniture."""
    # TODO: Implement this properly
    return svdata([{
                       'api_member_id': g.admiral.id, 'api_id': item.id, 'api_furniture_type': item.type,
                       'api_furniture_no': item.no, 'api_furniture_id': item.id
                   } for item in []])


@api_member.route('/slot_item', methods=['GET', 'POST'])
def slot_item():
    return svdata(MemberHelper.slot_info())


@api_member.route('/useitem', methods=['GET', 'POST'])
def useitem():
    # TODO: Implement this properly
    return svdata(MemberHelper.useitem())


@api_member.route('/kdock', methods=['GET', 'POST'])
def kdock():
    """Krafting docks."""
    return svdata(MemberHelper.kdock())


@api_member.route('/ndock', methods=['GET', 'POST'])
def ndock():
    return svdata(MemberHelper.rdock())


@api_member.route('/unsetslot', methods=['GET', 'POST'])
def unsetslot():
    return svdata(MemberHelper.unsetslot())


@api_member.route('/ship2', methods=['GET', 'POST'])
def ship2():
    """Fuck ship2."""
    """Agreed."""
    return redirect(url_for(".p_index"))


@api_member.route('/material', methods=['GET', 'POST'])
def material():
    return svdata(MemberHelper.material())


@api_member.route('/ship3', methods=['GET', 'POST'])
# After item change
def ship3():
    kanmusu_id = request.values.get('api_shipid')
    return svdata(MemberHelper.ship3(kanmusu_id))


@api_member.route('/preset_deck', methods=['GET', 'POST'])
def preset_deck():
    # TODO: Find what this does.
    return svdata({"api_max_num": len(g.admiral.fleets), "api_deck": {}})


@api_member.route('/record', methods=['GET', 'POST'])
def record():
    data = {
        "api_member_id": g.admiral.id,
        "api_nickname": g.admiral.name,
        "api_nickname_id": str(g.admiral.id),
        "api_cmt": "",
        "api_cmt_id": "",
        "api_photo_url": "",
        "api_rank": g.admiral.rank,
        "api_level": g.admiral.level,
        "api_experience": [
            g.admiral.experience,
            # Exp to next level
            sum(HQ_LEVEL[:g.admiral.level + 1])
        ],
        # api_war -> sorties
        "api_war": {
            "api_win": str(g.admiral.sortie_successes),
            "api_lose": str(g.admiral.sortie_total - g.admiral.sortie_successes),
            "api_rate": str(round((g.admiral.sortie_successes / g.admiral.sortie_total)
                                  if g.admiral.sortie_total else 0, 2))
        },
        # api_mission -> expeditions
        "api_mission": {
            "api_count": str(g.admiral.expedition_total),
            "api_success": str(g.admiral.expedition_successes),
            "api_rate": str(round(((g.admiral.expedition_total / g.admiral.expedition_successes) * 100)
                                  if g.admiral.expedition_successes else 0, 2))
            # Full percentage. Not rounded percentage. Stupid kc
        },
        "api_practice": {
            "api_win": str(g.admiral.pvp_successes),
            "api_lose": str(g.admiral.pvp_total - g.admiral.pvp_successes),
            "api_rate": str(round((g.admiral.pvp_total / g.admiral.pvp_successes)
                                  if g.admiral.pvp_successes else 0, 2))
        },
        "api_friend": 0,  # No idea
        "api_deck": len(g.admiral.fleets),
        "api_kdoc": len(g.admiral.docks_craft),
        "api_ndoc": len(g.admiral.docks_repair),
        "api_ship": [  # Current amount, max
            len(g.admiral.kanmusu),
            999999
        ],
        "api_slotitem": [
            len(g.admiral.equipment.all()),
            9999999
        ],
        "api_furniture": 8,  # Not sure
        "api_complate": [
            "0.0",
            "0.0"
        ],  # Not sure
        "api_large_dock": 1,
        "api_material_max": 1000000  # Maximum materials
    }
    return svdata(data)


@api_member.route("/mission", methods=["GET", "POST"])
def mission():
    # Gets list of expeditions.
    # This is a simple query that lists all expeditions.
    # If the admiral has completed them, it will respond with the appropriate state.
    # Note that expedition details are stored in api_start2.
    expd = Expedition.query.all()
    states = {}
    for e in expd:
        if e in g.admiral.expeditions:
            states[e.id] = 2
        else:
            states[e.id] = 0
    return svdata([OrderedDict(api_mission_id=id, api_state=state) for (id, state) in states.items()])


@api_member.route("/deck", methods=["GET", "POST"])
def fleets():
    return svdata([fleet(fleet_) for fleet_ in g.admiral.fleets])
