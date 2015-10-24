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
def ship3():
    kanmusu_id = request.values.get('api_shipid')
    return svdata(refit.ship3(kanmusu_id))