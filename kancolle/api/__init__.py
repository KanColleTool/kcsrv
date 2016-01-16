"""
kancolle/api -> Core API stuff. Bleh.
"""

from flask import Blueprint, g

from util import prepare_api_blueprint, load_datadump, svdata

api_core = Blueprint('api_core', __name__)
api_game = Blueprint('api_game', __name__)

prepare_api_blueprint(api_core)
prepare_api_blueprint(api_game)

@api_core.before_request
def load_api_start2():
    if not 'data_start2' in g:
        g.data_start2 = load_datadump("api_start2.json")


@api_core.route('/api_start2', methods=['GET', 'POST'])
def start2():
    return svdata(g.data_start2)
