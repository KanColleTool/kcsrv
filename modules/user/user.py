from flask import Blueprint
# from flask.ext.security import current_user
from util import *
from modules import placeholderdata
import generate_port
from . import AdmiralHelper

api_user = Blueprint('api_user', __name__)
prepare_api_blueprint(api_user)


@api_user.route('/api_req_member/get_incentive', methods=['GET', 'POST'])
def get_incentive():
    return svdata({
        'api_count': 0
    })  # What?


@api_user.route('/api_get_member/basic', methods=['GET', 'POST'])
def basic():
    admiral = get_token_admiral_or_error()
    return svdata(AdmiralHelper.get_admiral_basic_info())


@api_user.route('/api_get_member/furniture', methods=['GET', 'POST'])
def furniture():
    # TODO: Implement this properly
    admiral = get_token_admiral_or_error()
    return svdata([{
        'api_member_id': admiral.id,
        'api_id': item.id,
        'api_furniture_type': item.type,
        'api_furniture_no': item.no,
        'api_furniture_id': item.id
    } for item in []])


@api_user.route('/api_get_member/slot_item', methods=['GET', 'POST'])
def slot_item():
    # TODO: Implement this properly
    admiral = get_token_admiral_or_error()
    return svdata([{'api_id': item.id, 'api_slotitem_id': item.itemid, 'api_locked': 0} for item in []])


@api_user.route('/api_get_member/useitem', methods=['GET', 'POST'])
def useitem():
    # TODO: Implement this properly
    admiral = get_token_admiral_or_error()
    return svdata([{
        'api_member_id': admiral.id,
        'api_id': item.id,
        'api_value': item.count,
        'api_usetype': item.type,
        'api_category': item.category,
        'api_name': item.name,  # WHY
        'api_description': ["", ""],
        'api_price': 0,
        'api_count': item.count
    } for item in []])



@api_user.route('/api_get_member/kdock', methods=['GET', 'POST'])
def kdock():
    # TODO: Implement this properly
    admiral = get_token_admiral_or_error()
    return svdata([{
        'api_member_id': admiral.id,
        'api_id': dock.id,
        'api_state': dock.state,
        'api_created_ship_id': dock.ship,
        'api_complete_time': dock.complete,  # TODO: Convert this to JST
        'api_complete_time_str': dock.complete.strftime('%Y-%M-%d %H:%M:%S'),
        'api_item1': dock.fuel,
        'api_item2': dock.ammo,
        'api_item3': dock.steel,
        'api_item4': dock.baux,
        'api_item5': dock.cmats
    } for dock in []])


@api_user.route('/api_get_member/unsetslot', methods=['GET', 'POST'])
def unsetslot():
    # TODO: Figure out what the hell this even is!
    return svdata(placeholderdata.unsetslot)


@api_user.route('/api_port/port', methods=['GET', 'POST'])
def port():
    api_token = request.values.get('api_token', None)
    if api_token is None:
        abort(403)
    print(generate_port.generate_port(api_token))
    return svdata(generate_port.generate_port(api_token))


@api_user.route('/api_req_init/firstship', methods=['GET', 'POST'])
# Kancolle literally doesn't care, as long as it gets something back
def firstship():
    admiral = get_token_admiral_or_error()
    return svdata({'api_result_msg': 'shitty api is shitty', 'api_result': 1})


@api_user.route('/api_get_member/ship2', methods=['GET', 'POST'])
def ship2():
    return json.dumps(placeholderdata.ship2)  # FUCK YOU KANCOLLE AND YOUR SHITTY REQUIREMENTS

# Generic routes for anything not implemented.

@api_user.route('/api_req_init/<path:path>', methods=['GET', 'POST'])
def misc(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201})


@api_user.route('/api_get_member/<path:path>', methods=['GET', 'POST'])
def misc2(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201})
