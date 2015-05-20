from flask import Blueprint, redirect
# from flask.ext.security import current_user
from util import *
from modules.api import placeholderdata
from helpers import generate_port, AdmiralHelper, DockHelper

api_user = Blueprint('api_user', __name__)
prepare_api_blueprint(api_user)


@api_user.route('/api_get_member/material')
def material():
    """Resources such as fuel, ammo, etc..."""
    admiral = get_token_admiral_or_error()
    return svdata([
        {"api_id": n + 1,
         "api_member_id": admiral.id,
         "api_value": int(val)} for n, val in enumerate(admiral.resources.split(','))
    ])

@api_user.route('/api_req_member/get_incentive', methods=['GET', 'POST'])
def get_incentive():
    return svdata({
        'api_count': 0
    })  # What?

@api_user.route('/api_get_member/basic', methods=['GET', 'POST'])
def basic():
    """Basic admiral data."""
    return svdata(AdmiralHelper.get_admiral_basic_info())


@api_user.route('/api_get_member/furniture', methods=['GET', 'POST'])
def furniture():
    """Available furniture."""
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
    """Krafting docks."""
    admiral = get_token_admiral_or_error()
    return svdata(DockHelper.generate_dock_data(admiral)['cdock'])

@api_user.route('/api_get_member/ndock', methods=['POST'])
def ndock():
    """Repair dock endpoint."""
    admiral = get_token_admiral_or_error()
    return svdata(DockHelper.generate_dock_data(admiral)['rdock'])

@api_user.route('/api_get_member/unsetslot', methods=['GET', 'POST'])
def unsetslot():
    # TODO: Figure out what the hell this even is!
    return svdata(placeholderdata.unsetslot)


@api_user.route('/api_port/port', methods=['GET', 'POST'])
def port():
    """Port endpoint."""
    api_token = request.values.get('api_token', None)
    if api_token is None:
        abort(403)
    port = generate_port.generate_port(api_token)['api_data']
    return svdata(port)


@api_user.route('/api_get_member/ship2', methods=['GET', 'POST'])
def ship2():
    """Fuck ship2."""
    return redirect("/play/", code=301)

# Generic routes for anything not implemented.

@api_user.route('/api_req_init/<path:path>', methods=['GET', 'POST'])
def misc(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201})


@api_user.route('/api_get_member/<path:path>', methods=['GET', 'POST'])
def misc2(path):
    return svdata({'api_result_msg': '申し訳ありませんがブラウザを再起動し再ログインしてください。', 'api_result': 201})
