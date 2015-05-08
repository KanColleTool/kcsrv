#!/usr/bin/env python
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from helpers import generate_ship
from kcsrv import app
from db import *


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
    db.session.add(db.Role(name="admin", description="Allowed to access the admin panel"))
    db.session.add(db.Role(name="staff", description="Allowed to see restricted information"))
    db.session.commit()

@manager.command
def dlassets():
    commands.kcdownloader2.run()

@manager.command
def cheat_addship(id, admiral_id):
    ship = generate_ship.generate_new_ship(id)
    admiral = Admiral.query.filter_by(id=admiral_id)[0]
    if admiral:
        admiral.admiral_ships.append(ship)
    db.session.merge(admiral)
    db.session.commit()
    print("Added ship {}".format(ship.ship.name))

if __name__ == '__main__':
    manager.run()
