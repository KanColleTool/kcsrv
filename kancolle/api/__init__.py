"""
kancolle/api -> Core API stuff. Bleh.
"""

from flask import Blueprint, g
from .actions import api_actions
from .member import api_game as api_member
from .init import api_init

from util import prepare_api_blueprint, load_datadump, svdata


prepare_api_blueprint(api_actions)
prepare_api_blueprint(api_member)
prepare_api_blueprint(api_init)

@api_actions.before_request
def load_api_start2():
    if not 'data_start2' in g:
        g.data_start2 = load_datadump("api_start2.json")


@api_actions.route('/api_start2', methods=['GET', 'POST'])
def start2():
    return svdata(g.data_start2)
