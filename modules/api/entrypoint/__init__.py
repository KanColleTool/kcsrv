from flask import Blueprint
from util import prepare_api_blueprint

api_game = Blueprint('api_game', __name__)
prepare_api_blueprint(api_game)

from modules.api.entrypoint import gamestart_entry
from modules.api.entrypoint import refit_entry
