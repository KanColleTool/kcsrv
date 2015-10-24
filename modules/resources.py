from flask import Blueprint, send_from_directory

from app import app

resources = Blueprint('resources', __name__)

cfg = app.config

@resources.route('/resources/swf/ships/<path:ship>')
def get_ship(ship):
    return send_from_directory("kcs/resources/swf/ships", ship)

@resources.route('/resources/swf/<path:path>')
def resources_swf(path):
    return send_from_directory('kcs/resources/swf', path)

@resources.route('/sound/titlecall/<path:path>')
def sound(path):
    return send_from_directory('kcs/titlecall', path)

@resources.route('/sound/<path:path>')
def shipsound(path):
    return send_from_directory('kcs/sound/ship', path)

@resources.route('/<path:path>')
def kcs(path):
    return send_from_directory('kcs', path)
