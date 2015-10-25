from util import svdata
from flask import request,g
from helpers import gamestart
from . import api_game

@api_game.route('/api_req_init/firstship', methods=['GET', 'POST'])
# Kancolle literally doesn't care, as long as it gets something back
def firstship():
    shipid = request.values.get("api_ship_id")
    g.admiral.add_kanmusu(ship_api_id=shipid, fleet_number=1, position=0)
    return svdata({'api_result_msg': 'shitty api is shitty', 'api_result': 1})

@api_game.route('/api_port/port', methods=['GET', 'POST'])
def port():
    # return svdata(game_start.port())
    return svdata(gamestart.port())