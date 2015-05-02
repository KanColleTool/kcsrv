from flask import Blueprint, send_from_directory
from util import *

resources = Blueprint('resources', __name__)

@resources.route('/swf/ships/<path:ship>')
def get_ship(ship):
    return send_from_directory("kcs/resources/swf/ships", ship)

@resources.route('/swf/<path:path>')
def kcs(path):
    return send_from_directory('kcs', path)