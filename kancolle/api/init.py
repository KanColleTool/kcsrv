from flask import request, g, Blueprint

from db import Kanmusu
from util import svdata

api_init = Blueprint('api_init', __name__)


# First ship route
@api_init.route('/api_req_init/firstship', methods=['GET', 'POST'])
# Kancolle literally doesn't care, as long as it gets something back
def firstship():
    shipid = request.values.get("api_ship_id")
    # TODO: Validation
    k = Kanmusu(ship_api_id=shipid)
    g.admiral.add_kanmusu(k, fleet_number=1, position=0)
    return svdata({'api_result_msg': 'shitty api is shitty', 'api_result': 1})


@api_init.route('/api_req_member/get_incentive', methods=['GET', 'POST'])
def get_incentive():
    return svdata({
        'api_count': 0
    })  # What?
