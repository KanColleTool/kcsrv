from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import UserMixin, RoleMixin

import util

db = SQLAlchemy()

role__user = db.Table('role__user',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                      )


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ship = db.relationship("Ship", uselist=False)
    ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'))

    chance = db.Column(db.Integer, default=1)

    minfuel = db.Column(db.Integer, nullable=False, default=30)
    maxfuel = db.Column(db.Integer, nullable=False, default=30)
    minammo = db.Column(db.Integer, nullable=False, default=30)
    maxammo = db.Column(db.Integer, nullable=False, default=30)
    minsteel = db.Column(db.Integer, nullable=False, default=30)
    maxsteel = db.Column(db.Integer, nullable=False, default=30)
    minbaux = db.Column(db.Integer, nullable=False, default=30)
    maxbaux = db.Column(db.Integer, nullable=False, default=30)


class Fleet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="Unnamed")
    admiral_id = db.Column(db.Integer, db.ForeignKey('admiral.id'))

    ships = db.relationship("AdmiralShip", lazy='dynamic', order_by='AdmiralShip.local_fleet_num')


class Dock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Integer)
    complete = db.Column(db.BigInteger, nullable=True)
    fuel = db.Column(db.Integer, nullable=True)
    ammo = db.Column(db.Integer, nullable=True)
    steel = db.Column(db.Integer, nullable=True)
    baux = db.Column(db.Integer, nullable=True)
    cmats = db.Column(db.Integer, nullable=True)

    ship_id = db.Column(db.Integer, db.ForeignKey("admiral_ship.id"))
    ship = db.relationship("AdmiralShip", uselist=False)

    admiral_id = db.Column(db.Integer, db.ForeignKey("admiral.id"))


class AdmiralShip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admiral_id = db.Column(db.Integer, db.ForeignKey('admiral.id'))
    ship = db.relationship("Ship", uselist=False)
    ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'))

    fleet_id = db.Column(db.Integer, db.ForeignKey('fleet.id'))

    local_fleet_num = db.Column(db.Integer)
    local_ship_num = db.Column(db.Integer, nullable=False)

    # Unique ship-specific attributes
    ammo = db.Column(db.Integer)
    fuel = db.Column(db.Integer)
    fatigue = db.Column(db.Integer, default=49)

    exp = db.Column(db.Integer)
    level = db.Column(db.Integer)

    repair_base = db.Column(db.String())

    current_hp = db.Column(db.Integer)  # Oh dear.

    # Ship stats
    luck = db.Column(db.Integer, default=0)
    luck_eq = db.Column(db.Integer, default=0)
    firepower = db.Column(db.Integer, default=0)
    firepower_eq = db.Column(db.Integer, default=0)
    armour = db.Column(db.Integer, default=0)
    torpedo = db.Column(db.Integer, default=0)
    torpedo_eq = db.Column(db.Integer, default=0)
    antiair = db.Column(db.Integer, default=0)
    antiair_eq = db.Column(db.Integer, default=0)
    antisub = db.Column(db.Integer, default=0)
    evasion = db.Column(db.Integer, default=0)

    heartlocked = db.Column(db.Boolean, default=False)

    active = db.Column(db.Boolean, default=False, nullable=False)

    def __str__(self):
        return self.ship.name

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    afterlv = db.Column(db.Integer, nullable=True)
    aftership_num = db.Column(db.Integer, nullable=True)
    remodel_cost = db.Column(db.String())

    rarity = db.Column(db.Integer)
    broken = db.Column(db.String())

    ammo_max = db.Column(db.Integer)
    fuel_max = db.Column(db.Integer)

    name = db.Column(db.String)
    number = db.Column(db.Integer)
    stype = db.Column(db.Integer)

    voicef = db.Column(db.Integer)

    modern_use = db.Column(db.String)
    # Minimums
    luck_base = db.Column(db.Integer, default=0)
    firepower_base = db.Column(db.Integer, default=0)
    torpedo_base = db.Column(db.Integer, default=0)
    armour_base = db.Column(db.Integer, default=0)
    antiair_base = db.Column(db.Integer, default=0)
    antisub_base = db.Column(db.Integer, default=0)
    los_base = db.Column(db.Integer, default=0)
    evasion_base = db.Column(db.Integer, default=0)
    hp_base = db.Column(db.Integer, default=0)

    # Maximums
    luck_max = db.Column(db.Integer, default=0)
    firepower_max = db.Column(db.Integer, default=0)
    torpedo_max = db.Column(db.Integer, default=0)
    armour_max = db.Column(db.Integer, default=0)
    antiair_max = db.Column(db.Integer, default=0)
    antisub_max = db.Column(db.Integer, default=0)
    maxslots = db.Column(db.Integer, default=0)
    maxlos = db.Column(db.Integer, default=0)
    evasion_max = db.Column(db.Integer, default=0)

    maxhp = db.Column(db.Integer)
    srange = db.Column(db.Integer, default=0)

    kai = db.Column(db.Boolean, default=False)

    # Messages
    getmsg = db.Column(db.String(255))
    buildtime = db.Column(db.Integer)

    maxplanes = db.Column(db.String())

    def __str__(self):
        return self.name

class Admiral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    last_login = db.Column(db.DateTime)

    level = db.Column(db.Integer, default=1)
    rank = db.Column(db.Integer, default=8)
    experience = db.Column(db.Integer, default=0)
    tutorial_progress = db.Column(db.Integer, default=0)

    furniture = db.Column(db.String(), default="1,1,1,1,1,1")
    furniture_coins = db.Column(db.Integer, default=0)

    max_ships = db.Column(db.Integer, default=5000)
    max_equips = db.Column(db.Integer, default=10000)
    max_furniture = db.Column(db.Integer, default=10000)
    available_fleets = db.Column(db.Integer, default=1)
    available_cdocks = db.Column(db.Integer, default=4)
    available_rdocks = db.Column(db.Integer, default=4)

    sortie_successes = db.Column(db.Integer, default=0)
    sortie_total = db.Column(db.Integer, default=0)
    expedition_successes = db.Column(db.Integer, default=0)
    expedition_total = db.Column(db.Integer, default=0)
    pvp_successes = db.Column(db.Integer, default=0)
    pvp_total = db.Column(db.Integer, default=0)

    admiral_ships = db.relationship(AdmiralShip, backref='admiral', lazy='dynamic')

    resources = db.Column(db.String())

    fleets = db.relationship(Fleet, backref='admiral', lazy='dynamic')

    # If this is false...
    # 1) api_req_init is enabled
    #   2) setup() is enabled, which means a new fleet will be automatically added, and two docks of each kind
    # If this is true...
    #   1) api_req_init will be disabled
    #   2) setup() is disabled.
    setup = db.Column(db.Boolean())
    docks = db.relationship("Dock", backref='admiral', lazy='dynamic', order_by='Dock.id')

    lastaction = db.Column(db.DateTime)

    def __str__(self):
        return "Admiral " + self.user.nickname


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean)

    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    confirmed_at = db.Column(db.DateTime())

    nickname = db.Column(db.String(255), unique=True, nullable=False)
    api_token = db.Column(db.String(40), default=lambda: util.generate_api_token(), unique=True)

    admiral = db.relationship(Admiral, backref='user', uselist=False)

    roles = db.relationship('Role', secondary=role__user, backref=db.backref('users', lazy='dynamic'))  # Fix roles

    def __str__(self):
        return self.email



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)

    def __str__(self):
        return self.name
