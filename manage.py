#!/usr/bin/env python3
import os
import sqlalchemy
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Server
# from helpers import ShipHelper
from kcsrv import app
from db import db, Role
from offline import dbpopulate, kccheat

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


@manager.command
def setup():
    print("Installing default roles...")
    db.session.add(Role(name="admin", description="Allowed to access the admin panel"))
    db.session.add(Role(name="staff", description="Allowed to see restricted information"))
    db.session.commit()


@manager.command
def cheat(where, id, admiral_id, action=None):
    if where == "quest":
        if action == "add":
            kccheat.quest_add(admiral_id, id)
        elif action == "complete":
            kccheat.quest_complete(admiral_id, id)
    elif where == "ship":
        kccheat.ship_add(admiral_id, id)
    elif where == "equip":
        kccheat.equip_add(admiral_id, id)
    else:
        print("Unknown cheat")


@manager.command
def update_db():
    """Update all parts of the DB"""
    dbpopulate.ships()
    dbpopulate.equip()
    dbpopulate.items()
    dbpopulate.recipe_resources()
    dbpopulate.expeditions()
    try:
        setup()
    except sqlalchemy.exc.IntegrityError:
        pass


if __name__ == '__main__':
    manager.run()
