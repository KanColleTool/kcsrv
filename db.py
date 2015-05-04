from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import UserMixin, RoleMixin
from sqlalchemy.dialects.postgresql import ARRAY
import util

db = SQLAlchemy()

role__user = db.Table('role__user',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                      )



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)

    def __unicode__(self):
        return self.name

class Dock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Integer)
    ship = db.Column(db.Integer, nullable=True)
    complete = db.Column(db.Integer, nullable=True)
    fuel = db.Column(db.Integer, nullable=True)
    ammo = db.Column(db.Integer, nullable=True)
    steel = db.Column(db.Integer, nullable=True)
    baux = db.Column(db.Integer, nullable=True)
    cmats = db.Column(db.Integer, nullable=True)

# I give no fucks

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    afterlv = db.Column(db.Integer, nullable=True)
    aftershipid = db.Column(db.Integer, nullable=True)
    remodel_cost = db.Column(ARRAY(db.Integer))

    rarity = db.Column(db.Integer)
    broken = db.Column(ARRAY(db.Integer))

    ammo_max = db.Column(db.Integer)
    fuel_max = db.Column(db.Integer)

    name = db.Column(db.String)
    number = db.Column(db.Integer)
    stype = db.Column(db.Integer)

    voicef = db.Column(db.Integer)

    modern_use = db.Column(ARRAY(db.Integer))
    # Minimums
    luck_base = db.Column(db.Integer)
    firepower_base = db.Column(db.Integer)
    armour_base = db.Column(db.Integer)
    antiair_base = db.Column(db.Integer)
    antisub_base = db.Column(db.Integer)
    los_base = db.Column(db.Integer)
    evasion_base = db.Column(db.Integer)

    # Maximums
    luck_max = db.Column(db.Integer)
    firepower_max = db.Column(db.Integer)
    armour_max = db.Column(db.Integer)
    antiair_max = db.Column(db.Integer)
    antisub_max = db.Column(db.Integer)
    maxslots = db.Column(db.Integer)
    maxlos = db.Column(db.Integer)
    evasion_max = db.Column(db.Integer)

    maxhp = db.Column(db.Integer)
    srange = db.Column(db.Integer)

    # Messages
    getmsg = db.Column(db.String(255))
    buildtime = db.Column(db.Integer)

    maxplanes = db.Column(ARRAY(db.Integer))



    def __init__(*args, **kwargs): super().__init__(*args, **kwargs)


class AdmiralShip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admiralid = db.Column(db.Integer, db.ForeignKey('admiral.id'))
    ship = db.relationship(Ship)
    ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'))

    fleet_id = db.Column(db.Integer)

    # Unique ship-specific attributes
    ammo = db.Column(db.Integer)
    fuel = db.Column(db.Integer)
    fatigue = db.Column(db.Integer, default=49)

    exp = db.Column(db.Integer)
    level = db.Column(db.Integer)

    repair_base = db.Column(ARRAY(db.Integer))

    # Ship stats
    luck = db.Column(db.Integer)
    luck_eq = db.Column(db.Integer)
    firepower = db.Column(db.Integer)
    firepower_eq = db.Column(db.Integer)
    armour = db.Column(db.Integer)
    torpedo = db.Column(db.Integer)
    torpedo_eq = db.Column(db.Integer)
    antiair = db.Column(db.Integer)
    antiair_eq = db.Column(db.Integer)
    antisub = db.Column(db.Integer)



class Admiral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    last_login = db.Column(db.DateTime)

    level = db.Column(db.Integer, default=1)
    rank = db.Column(db.Integer, default=8)
    experience = db.Column(db.Integer, default=0)
    tutorial_progress = db.Column(db.Integer, default=0)

    furniture = db.Column(db.String(100), default="1,38,77,110,151,168")
    furniture_coins = db.Column(db.Integer, default=0)

    max_ships = db.Column(db.Integer, default=500)
    max_equips = db.Column(db.Integer, default=1000)
    max_furniture = db.Column(db.Integer, default=0)
    available_fleets = db.Column(db.Integer, default=1)
    available_cdocks = db.Column(db.Integer, default=2)
    available_rdocks = db.Column(db.Integer, default=2)

    sortie_successes = db.Column(db.Integer, default=0)
    sortie_total = db.Column(db.Integer, default=0)
    expedition_successes = db.Column(db.Integer, default=0)
    expedition_total = db.Column(db.Integer, default=0)
    pvp_successes = db.Column(db.Integer, default=0)
    pvp_total = db.Column(db.Integer, default=0)

    admiral_ships = db.relationship(AdmiralShip, backref='admiral', lazy='dynamic')


    #repair_docks = db.relationship("")

    def __unicode__(self):
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

    roles = db.relationship('Role', secondary=role__user, backref=db.backref('users', lazy='dynamic')) # Fix roles

    def __unicode__(self):
        return self.email
