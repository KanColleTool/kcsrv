from flask import request,g

from util import svdata
from . import api_game


@api_game.route('/api_req_init/firstship', methods=['GET', 'POST'])
# Kancolle literally doesn't care, as long as it gets something back
def firstship():
    shipid = request.values.get("api_ship_id")
    g.admiral.add_kanmusu(ship_api_id=shipid, fleet_number=1, position=0)
    return svdata({'api_result_msg': 'shitty api is shitty', 'api_result': 1})

@api_game.route('/api_req_member/get_incentive', methods=['GET', 'POST'])
def get_incentive():
    return svdata({
        'api_count': 0
    })  # What?


@api_game.route('/api_get_member/basic', methods=['GET', 'POST'])
def basic():
    """Basic admiral data."""
    return svdata(g.admiral.basic())


@api_game.route('/api_get_member/furniture', methods=['GET', 'POST'])
def furniture():
    """Available furniture."""
    # TODO: Implement this properly
    return svdata([{
        'api_member_id': g.admiral.id, 'api_id': item.id, 'api_furniture_type': item.type, 'api_furniture_no': item.no, 'api_furniture_id': item.id
    } for item in []])


@api_game.route('/api_get_member/slot_item', methods=['GET', 'POST'])
def slot_item():
    return svdata(g.admiral.slot_info())


@api_game.route('/api_get_member/useitem', methods=['GET', 'POST'])
def useitem():
    # TODO: Implement this properly
    return svdata(g.admiral.useitem())


@api_game.route('/api_get_member/kdock', methods=['GET', 'POST'])
def kdock():
    """Krafting docks."""
    return svdata(g.admiral.kdock())

@api_game.route('/api_get_member/unsetslot', methods=['GET', 'POST'])
def unsetslot():
    return svdata(g.admiral.unsetslot())


@api_game.route('/api_port/port', methods=['GET', 'POST'])
def port():
    # return svdata(game_start.port())
    # 2 lazy to go through and fix the port showing up twice, so here's this instead
    return svdata(g.admiral.port()["api_data"])


@api_game.route('/api_get_member/ship2', methods=['GET', 'POST'])
def ship2():
    """Fuck ship2."""
    """Agreed."""
    return svdata({})