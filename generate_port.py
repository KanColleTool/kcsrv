import json
import db
import util


def generate_port(api_token):
    # First, get the admiral.
    admiral = util.get_token_admiral_or_error(api_token)
    assert isinstance(admiral, db.Admiral)
    # Initial KanColle reply.
    port2 = {
        "api_result_msg": "成功",
        "api_result": 1,
        "api_data": {}

    }
    # TODO: Log entry
    port2["api_data"]['api_log'] = [
        {
            "api_state": "0",
            "api_no": 0,
            "api_type": "1",
            "api_message": "ayy lmao"
        }
    ]
    # Background music?
    port2["api_data"]["api_p_bgm_id"] = 100
    # This sets the parallel quest count. Don't know what higher values do, default is 5.
    port2["api_data"]["api_parallel_quest_count"] = 5
    # Combined flag? Event data probably.
    port2["api_data"]["api_combined_flag"] = 0
    # API basic - a replica of api_get_member/basic
    port2['api_data']['api_basic'] = {
        'api_member_id': admiral.id,
        'api_nickname': admiral.user.nickname,
        'api_nickname_id': admiral.user.id,
        'api_active_flag': 1,
        'api_starttime': util.millisecond_timestamp(),
        'api_level': admiral.level,
        'api_rank': admiral.rank,
        'api_experience': admiral.experience,
        'api_fleetname': "Fleet One",
        'api_comment': "",
        'api_comment_id': "",
        'api_max_chara': admiral.max_ships,
        'api_max_slotitem': admiral.max_equips,
        'api_max_kagu': admiral.max_furniture,
        'api_playtime': 1,
        'api_tutorial': "0",
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
        'api_pt_lose': admiral.pvp_total - admiral.pvp_successes,  # These two aren't even in the game...
        'api_pt_challenged': 0,
        'api_pt_challenged_win': 0,
        'api_firstflag': 1,  # Disables the opening stuff, and skips straight to the game.
        'api_tutorial_progress': 100,
        'api_pvp': [0, 0]
    }

    return port2