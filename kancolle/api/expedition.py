"""Expedition blueprint."""
from flask import Blueprint

from util import prepare_api_blueprint

api_mission = Blueprint("api_mission", __name__)
prepare_api_blueprint(api_mission)