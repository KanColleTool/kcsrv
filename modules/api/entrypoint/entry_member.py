from flask import request
from . import api_game
from helpers import member
from util import svdata

@api_game.route('/api_req_member/get_incentive', methods=['GET', 'POST'])
def get_incentive():
    return svdata({
        'api_count': 0
    })  # What?


@api_game.route('/api_get_member/basic', methods=['GET', 'POST'])
def basic():
    """Basic admiral data."""
    return svdata(member.basic())


@api_game.route('/api_get_member/furniture', methods=['GET', 'POST'])
def furniture():
    """Available furniture."""
    # TODO: Implement this properly
    return svdata([{
        'api_member_id': admiral.id, 'api_id': item.id, 'api_furniture_type': item.type, 'api_furniture_no': item.no, 'api_furniture_id': item.id
    } for item in []])

@api_game.route('/api_get_member/slot_item', methods=['GET', 'POST'])
def slot_item():
    return svdata(member.slot_info())


@api_game.route('/api_get_member/useitem', methods=['GET', 'POST'])
def useitem():
    # TODO: Implement this properly
    return svdata(member.useitem())


@api_game.route('/api_get_member/kdock', methods=['GET', 'POST'])
def kdock():
    """Krafting docks."""
    return svdata(member.kdock())

@api_game.route('/api_get_member/unsetslot', methods=['GET', 'POST'])
def unsetslot():
    return svdata(member.unsetslot())

@api_game.route('/api_get_member/ship2', methods=['GET', 'POST'])
def ship2():
    """Fuck ship2."""
    """Agreed."""
    return svdata({})

@api_game.route('/api_get_member/material', methods=['GET', 'POST'])
def material():
    return svdata(member.material())

@api_game.route('/api_get_member/ship3', methods=['GET', 'POST'])
# After item change
def ship3():
    kanmusu_id = request.values.get('api_shipid')
    return svdata(member.ship3(kanmusu_id))
