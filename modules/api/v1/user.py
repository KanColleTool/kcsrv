from flask import Blueprint
# from flask.ext.security import current_user
from util import *
# from db import AdmiralShip,Quest
from helpers import AdmiralHelper, ItemHelper
from helpers import gamestart, data, QuestHelper, ShipHelper


api_user = Blueprint('api_user', __name__)
prepare_api_blueprint(api_user)


@api_user.route('/api_get_member/material', methods=['GET', 'POST'])
def material():
    """Resources such as fuel, ammo, etc..."""
    admiral = get_token_admiral_or_error()
    return svdata(gamestart.get_admiral_resources_api_data(admiral))


@api_user.route('/api_get_member/mapinfo', methods=['GET', 'POST'])
def mapinfo():
    return svdata(AdmiralHelper.get_admiral_sorties())


@api_user.route('/api_get_member/questlist', methods=['GET', 'POST'])
# My god, he rebuilds the questlist every time you (de)activate a quest...
def questlist():
    import math
    page_number = request.values.get('api_page_no', None)
    data = {}
    admiral = get_token_admiral_or_error()
    questlist = QuestHelper.get_questlist_ordered(admiral)
    data['api_count'] = len(questlist)
    data['api_page_count'] = int(math.ceil(data['api_count'] / 5))
    data["api_disp_page"] = int(page_number)
    data["api_list"] = []
    for admiral_quest, quest in questlist:
        data["api_list"].append({
            "api_no": quest.id, "api_category": quest.category, "api_type": quest.frequency, "api_state": admiral_quest.state, "api_title": quest.title, "api_detail": quest.detail, "api_get_material": quest.reward.to_list(), "api_bonus_flag": quest.bonus_flag, "api_progress_flag": admiral_quest.progress, "api_invalid_flag": quest.invalid_flag
        })
    return svdata(data)


@api_user.route('/api_get_member/ship3', methods=['GET', 'POST'])
# Heh
def ship3():
    admiral = get_token_admiral_or_error()
    # No idea.
    # spi_sort_order = request.values.get('spi_sort_order')
    # spi_sort_order = request.values.get('api_sort_key')
    admiral_ship_id = request.values.get('api_shipid')
    data = {
        "api_ship_data": [ShipHelper.get_admiral_ship_api_data(
            admiral_ship_id)], "api_deck_data": AdmiralHelper.get_admiral_deck_api_data(
            admiral), "api_slot_data": ItemHelper.get_slottype_list(admiral=admiral)
    }
    return svdata(data)


@api_user.route('/api_get_member/test', methods=['GET', 'POST'])
def test():
    return svdata({})


# Generic routes for anything not implemented.

@api_user.route('/api_req_init/<path:path>', methods=['GET', 'POST'])
def misc(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201})


@api_user.route('/api_get_member/<path:path>', methods=['GET', 'POST'])
def misc2(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201})
