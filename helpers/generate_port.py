import db
import util
from helpers import AdmiralHelper

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
    port2['api_data']['api_basic'] = AdmiralHelper.get_admiral_basic_info()

    return port2