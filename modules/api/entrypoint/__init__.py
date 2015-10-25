from flask import Blueprint

from util import prepare_api_blueprint

api_game = Blueprint('api_game', __name__)
prepare_api_blueprint(api_game)

from modules.api.entrypoint import entry_member
from modules.api.entrypoint import entry_gamestart
from modules.api.entrypoint import entry_refit

