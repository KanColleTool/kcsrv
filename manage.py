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
    """Give the specified admiral a ship."""
    ship = generate_ship.generate_new_ship(id)
    admiral = Admiral.query.filter_by(id=admiral_id)[0]
    if admiral:
        admiral.admiral_ships.append(ship)
    db.session.merge(admiral)
    db.session.commit()
    print("Added ship {}".format(ship.ship.name))

@manager.command
def update_db():
    """Merge the ships DB from api_start.json into the DB"""
    dump = util.load_datadump('api_start2.json')
    # Truncate ships table.
    # db.db.session.query(db.Ship).delete()
    # Load ships from dump
    ships = dump['api_mst_ship']
    count = 0
    for ship in ships:
        s = db.Ship(
            # Misc ship stats
            id = ship['api_id'],
            rarity = ship['api_backs'],
            broken = ship['api_broken'],
            name = ship['api_name'],
            number = ship['api_sortno'],
            stype = ship['api_stype'],
            modern_use = ship['api_powup'],
            voicef = ship['api_voicef'],
            getmsg = ship['api_getmes'],
            srange = ship['api_leng'],
            buildtime = ship['api_buildtime'],
            kai = '改' in ship['api_name'],
            # Remodel
            afterlv = ship['api_afterlv'],
            aftershipid = ship['api_aftershipid'],
            remodel_cost = ','.join([str(ship['api_afterfuel']), str(ship['api_afterbull'])]),
            # Minimums
            luck_base = ship['api_luck'][0],
            firepower_base = ship['api_houg'][0],
            armour_base = ship['api_souk'][0],
            torpedo_base = ship['api_raig'][0],
            antiair_base = ship['api_tyku'][0],
            antisub_base = 0,
            los_base = 0,
            evasion_base = 0,
            hp_base = ship['api_taik'][0],
            # Maximums
            luck_max = ship['api_luck'][1],
            firepower_max = ship['api_houg'][1],
            armour_max = ship['api_souk'][1],
            torpedo_max = ship['api_raig'][1],
            antiair_max = ship['api_tyku'][1],
            antisub_max = 0,
            maxhp = ship['api_taik'][1],
            maxslots = ship['api_slot_num'],
            ammo_max = ship['api_bull_max'],
            fuel_max = ship['api_fuel_max'],
            maxlos = 0,
            evasion_max = 0,
            maxplanes = ','.join(str(x) for x in ship['api_maxeq'])
        )
        # ugh
        db.db.session.merge(s)
        print("Added ship {} - {}".format(ship['api_id'], ship['api_name']))
        count += 1
    db.db.session.commit()
    print("Updated database, {} entries merged..".format(count))

if __name__ == '__main__':
    manager.run()
