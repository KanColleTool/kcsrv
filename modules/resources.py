from flask import Blueprint, send_from_directory

from util import *
from app import app

try:
    import requests
except ImportError:
    requests = None
try:
    import pathlib
except ImportError:
    # Reraise.
    raise ImportError("You must be running Python 3.4 or newer, or using a python with a backported pathlib module.")

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
    if cfg['AUTODL_SOUND']:
        if os.path.exists('kcs/sound/ship/{}'.format(path)): return send_from_directory('kcs/sound/ship', path)
        # Gotcha, you bastard API name obfuscation
        p = pathlib.PurePath(path).parts[0]
        if not os.path.exists('kcs/sound/ship'): os.makedirs('kcs/sound/ship')
        if not os.path.exists('kcs/sound/ship/{}'.format(p)):
                os.makedirs('kcs/sound/ship/{}'.format(p))
        for x in range(0, 50):
            r = requests.get("http://203.104.209.39/kcs/sound/{}/{}.mp3".format(p, x), stream=True)
            if r:
                with open("kcs/sound/ship/{}/{}.mp3".format(p, x), 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
                print("Downloaded {}".format(x))
            else:
                print("Could not download {}".format(x))
    return send_from_directory('kcs/sound/ship', path)


@resources.route('/<path:path>')
def kcs(path):
    return send_from_directory('kcs', path)