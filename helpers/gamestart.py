from flask import g

import util
from . import member


def port():
    admiral = g.admiral
    response = {}
    # TODO: Log entry
    response['api_log'] = [{
        "api_state": "0", "api_no": 0, "api_type": "1", "api_message": "ayy lmao"
    }]
    # Background music?
    response["api_p_bgm_id"] = 100
    # This sets the parallel quest count. Don't know what higher values do, default is 5.
    # I set it to ten because fuck the police
    response["api_parallel_quest_count"] = 10
    # Combined flag? Event data probably.
    response["api_combined_flag"] = 0
    # API basic - a replica of api_get_member/basic
    response['api_basic'] = util.merge_two_dicts(member.basic(), {
        'api_medals': 0, 'api_large_dock': 0
    })
    # Fleets.
    response['api_deck_port'] = [member.fleet(fleet) for fleet in admiral.fleets]
    # Materials.
    response['api_material'] = member.material()

    response['api_ship'] = [member.kanmusu(kanmusu) for kanmusu in admiral.kanmusu if kanmusu.active]

    # Generate ndock.
    response['api_ndock'] = member.rdock()
    return response
