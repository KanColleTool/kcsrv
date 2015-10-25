from flask import g,request
from util import svdata
from helpers import refit
from . import api_game
from db import db,Kanmusu

@api_game.route('/api_req_kaisou/slotset', methods=['GET', 'POST'])
# Change Item
def slotset():
    id = request.values.get("api_id")
    equip_id = request.values.get("api_item_id")
    slot = request.values.get("api_slot_idx")

    Kanmusu.get(id).equip(admiral_equip_id=equip_id,slot=slot)
    db.session.commit()
    return svdata({'api_result_msg': 'ok', 'api_result': 1})


@api_game.route('/api_get_member/ship3', methods=['GET', 'POST'])
# After item change
def ship3():
    kanmusu_id = request.values.get('api_shipid')
    return svdata(refit.ship3(kanmusu_id))

@api_game.route('/api_req_kaisou/powerup', methods=['GET', 'POST'])
# Modernization
def powerup():
    id = request.values.get("api_id")
    id_items = request.values.get("api_id_items").split(',') #How mean girls aren't items
    result = Kanmusu.get(id).modernize(id_items)
    db.session.commit()
    return svdata(refit.powerup(id,result))

@api_game.route('/api_req_kaisou/remodeling', methods=['GET', 'POST'])
# Remodeling
def remodeling():
    id = request.values.get("api_id")
    Kanmusu.get(id).remodel() # If it only were that easy...
    return svdata({})

@api_game.route('/api_get_member/material', methods=['GET', 'POST'])
# Remodeling
def material():
    return svdata(refit.material())