from flask import Blueprint, g
from flask.ext.security import current_user
from util import *

api_user = Blueprint('api_user', __name__)
prepare_api_blueprint(api_user)

@api_user.route('/api_req_member/get_incentive', methods=['GET', 'POST'])
def get_incentive():
	return svdata({
		'api_count': 0
	})

@api_user.route('/api_get_member/basic', methods=['GET', 'POST'])
def basic():
	admiral = get_token_admiral_or_error()
	return svdata({
		'api_member_id': admiral.id,
		'api_nickname': admiral.user.nickname,
		'api_nickname_id': admiral.user.id,
		'api_active_flag': 1,
		'api_starttime': millisecond_timestamp(),
		'api_level': admiral.level,
		'api_rank': admiral.rank,
		'api_experience': admiral.experience,
		'api_fleetname': None,
		'api_comment': "",
		'api_comment_id': "",
		'api_max_chara': admiral.max_ships,
		'api_max_slotitem': admiral.max_equips,
		'api_max_kagu': admiral.max_furniture,
		'api_playtime': 0,
		'api_tutorial': (admiral.tutorial_progress < 100),
		'api_furniture': admiral.furniture.split(','),
		'api_count_deck': admiral.available_fleets,
		'api_count_kdock': admiral.available_cdocks,
		'api_count_ndock': admiral.available_rdocks,
		'api_fcoin': admiral.furniture_coins,
		'api_st_win': admiral.sortie_successes,
		'api_st_lose': admiral.sortie_total - admiral.sortie_successes,
		'api_ms_count': admiral.expedition_total,
		'api_ms_success': admiral.expedition_successes,
		'api_pt_win': admiral.pvp_successes,
		'api_pt_lose': admiral.pvp_total - admiral.pvp_successes,
		# These two aren't even in the game...
		'api_pt_challenged': 0,
		'api_pt_challenged_win': 0,
		'api_firstflag': 0,
		'api_tutorial_progress': admiral.tutorial_progress,
		# Why is this here? It's always [0, 0]!
		'api_pvp': [0, 0]
	})

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
	return svdata([{
		'api_id': item.id,
		'api_slotitem_id': item.itemid,
		# ...why?
		'api_locked': 0
	} for item in []])

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
		'api_name': item.name,
		# WHY
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
		'api_complete_time': dock.complete,
		# TODO: Convert this to JST
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
	return svdata({})
