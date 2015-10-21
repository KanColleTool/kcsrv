#!/usr/bin/env python3
import os

from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from helpers import ShipHelper
from kcsrv import app
from db import db,Ship,Role
from offline import dbpopulate,kccheat
import util

if not os.path.exists('./config.py'):
    print("Your config file does not exist. "
          "Create it by copying config.example.py to config.py and editing the required variables.")
    exit(1)

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', use_reloader=True))

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

from commands.user import manager as user_manager

manager.add_command('user', user_manager)

import commands.kcdownloader2

@manager.command
def setup():
    print("Installing default roles...")
    db.session.add(Role(name="admin", description="Allowed to access the admin panel"))
    db.session.add(Role(name="staff", description="Allowed to see restricted information"))
    db.session.commit()

@manager.command
def dlassets():
    commands.kcdownloader2.run()

@manager.command
def cheat_addship(id, admiral_id):
    """Give the specified admiral a ship."""
    admiral = Admiral.query.filter_by(id=admiral_id).first()
    ship = ShipHelper.generate_new_ship(id, None)
    ship.local_ship_num = len(admiral.admiral_ships.all())
    if admiral:
        admiral.admiral_ships.append(ship)
    db.session.add(admiral)
    db.session.commit()
    print("Added ship {}".format(ship.ship.name))

@manager.command
def cheat(where,id, admiral_id,action=None):
    if where == "quest":
        if action == "add":
            kccheat.quest_add(admiral_id,id)
        elif action == "complete":
            kccheat.quest_complete(admiral_id,id)
    elif where == "ship":
        kccheat.ship_add(admiral_id,id)
    elif where == "item":
        kccheat.item_add(admiral_id,id)
    else:
        print("Unknown cheat")




@manager.command
def update_db():
    """Merge the ships DB from api_start.json into the DB"""
    dbpopulate.ships()
    # Truncate ships table.
    # db.db.session.query(db.Ship).delete()
    # Load ships from dump
    dbpopulate.items()

if __name__ == '__main__':
    manager.run()
