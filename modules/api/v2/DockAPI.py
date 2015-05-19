import json
import time

from flask import Blueprint

import util

DockAPIv2 = Blueprint("DockAPIv2", __name__)

@DockAPIv2.route("/<token>/cdock/<id>")
def get_cdock(token, id):
    try:
        dockid = int(id) if id != "all" else id
    except ValueError:
        return "Invalid Dock ID", 400
    admiral = util.get_admiral_v2_from_id_or_token(token)
    if not admiral:
        return "Invalid API token/ID", 404
    try:
        if admiral.available_rdocks-1 < dockid:
            return "Invalid Dock ID", 400
    except TypeError: pass
    if id == "all":
        return json.dumps({"docks": [{
            "id": dockid,
            "shipbuiltid": dock.ship.ship.id if dock.ship is not None else 0,
            "completetime": dock.complete,
            "state": 0 if dock.complete is None
            else 2 if dock.complete > time.time()
            else 3 if dock.complete < time.time() else -1,
            "resources": ','.join([str(x) for x in [dock.fuel, dock.ammo, dock.steel, dock.baux, dock.cmats]])
        } for dock in admiral.docks.all()[0:4]]}), 200, {"Content-Type": "application/json"}
    else:
        cdock = admiral.docks.all()[dockid]
        print(admiral.docks.all(), dockid, cdock)
        return json.dumps({"docks": [{
            "id": dockid,
            "shipbuiltid": cdock.ship.ship.id if cdock.ship is not None else 0,
            "completetime": cdock.complete,
            "state": 0 if cdock.complete is None
            else 2 if cdock.complete > time.time()
            else 3 if cdock.complete < time.time() else -1,
            "resources": ','.join([str(x) for x in [cdock.fuel, cdock.ammo, cdock.steel, cdock.baux, cdock.cmats]])
        }]}), 200, {"Content-Type": "application/json"}

@DockAPIv2.route("/<token>/rdock/<id>")
def get_rdock(token, id):
    try:
        dockid = int(id)+1 if id != "all" else id
    except ValueError:
        return "Invalid Dock ID", 400
    admiral = util.get_admiral_v2_from_id_or_token(token)
    if not admiral:
        return "Invalid API token/ID", 404
    try:
        if admiral.available_rdocks-1 < dockid:
            return "Invalid Dock ID", 400
    except TypeError: pass
    if id == "all":
        return json.dumps({"docks": [{
            "id": dockid,
            "shipbuiltid": dock.ship.ship.id if dock.ship is not None else 0,
            "completetime": dock.complete,
            "state": 0 if dock.complete is None
            else 2 if dock.complete > time.time()
            else 3 if dock.complete < time.time() else -1,
            "resources": ','.join([str(x) for x in [dock.fuel, dock.ammo, dock.steel, dock.baux, dock.cmats]])
        } for dock in admiral.docks.all()[4:8]]}), 200, {"Content-Type": "application/json"}
    else:
        cdock = admiral.docks.all()[dockid+4]
        return json.dumps({"docks": [{
            "id": dockid,
            "shipbuiltid": cdock.ship.ship.id if cdock.ship is not None else 0,
            "completetime": cdock.complete,
            "state": 0 if cdock.complete is None
            else 2 if cdock.complete > time.time()
            else 3 if cdock.complete < time.time() else -1,
            "resources": ','.join([str(x) for x in [cdock.fuel, cdock.ammo, cdock.steel, cdock.baux, cdock.cmats]])
        }]}), 200, {"Content-Type": "application/json"}