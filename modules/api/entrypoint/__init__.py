from flask import Blueprint

from util import prepare_api_blueprint

api_game = Blueprint('api_game', __name__)
prepare_api_blueprint(api_game)

from modules.api.entrypoint import member
from modules.api.entrypoint import actions

