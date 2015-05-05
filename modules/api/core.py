from flask import Blueprint, g
from util import *

api_core = Blueprint('api_core', __name__)
prepare_api_blueprint(api_core)


@api_core.before_request
def load_api_start2():
    if not 'data_start2' in g:
        g.data_start2 = load_datadump("api_start2.json")


@api_core.route('/api_start2', methods=['GET', 'POST'])
def start2():
    return svdata(g.data_start2)
