from flask import request, g

from util import svdata
from db import db, Kanmusu
from . import api_game
from helpers import ActionsHelper

""""" Game Start Begin """""


@api_game.route('/api_port/port', methods=['GET', 'POST'])
def port():
    return svdata(ActionsHelper.port())


@api_game.route('/api_req_init/firstship', methods=['GET', 'POST'])
# Kancolle literally doesn't care, as long as it gets something back
def firstship():
    shipid = request.values.get("api_ship_id")
    g.admiral.add_kanmusu(ship_api_id=shipid, fleet_number=1, position=0)
    return svdata({'api_result_msg': 'shitty api is shitty', 'api_result': 1})


""""" Game Start End """""

""""" Refit Begin """""


@api_game.route('/api_req_kaisou/slotset', methods=['GET', 'POST'])
# Change Item
def slotset():
    id = request.values.get("api_id")
    equip_id = request.values.get("api_item_id")
    slot = request.values.get("api_slot_idx")

    Kanmusu.get(id).equip(admiral_equip_id=equip_id, slot=slot)
    db.session.commit()
    return svdata({})


@api_game.route('/api_req_kaisou/powerup', methods=['GET', 'POST'])
# Modernization
def powerup():
    id = request.values.get("api_id")
    id_items = request.values.get("api_id_items").split(',')  # How mean girls aren't items
    result = Kanmusu.get(id).modernize(id_items)
    db.session.commit()
    return svdata(ActionsHelper.powerup(id, result))


@api_game.route('/api_req_kaisou/remodeling', methods=['GET', 'POST'])
# Remodeling
def remodeling():
    id = request.values.get("api_id")
    Kanmusu.get(id).remodel()  # If it only were that easy...
    return svdata({})


""""" Refit End """""
