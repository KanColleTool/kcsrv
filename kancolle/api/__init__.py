"""
kancolle/api -> Core API stuff. Bleh.
"""

from flask import g
from util import prepare_api_blueprint, load_datadump, svdata
from .actions import api_actions, api_user
from .init import api_init
from .member import api_member as api_member
from .expedition import api_mission

prepare_api_blueprint(api_actions)
prepare_api_blueprint(api_member)
prepare_api_blueprint(api_init)
prepare_api_blueprint(api_user)


@api_actions.before_request
def load_api_start2():
    if not 'data_start2' in g:
        g.data_start2 = load_datadump("api_start2.json")


@api_actions.route('/api_start2', methods=['GET', 'POST'])
def start2():
    return svdata(g.data_start2)
