from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import UserMixin, RoleMixin
from util import generate_api_token
from constants import *
db = SQLAlchemy()

class Admiral(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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

    resource_id = db.Column(db.Integer,db.ForeignKey("resource.id"))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    admiral_ships = db.relationship("AdmiralShip", backref='admiral', lazy='dynamic')
    resources = db.relationship("Resource")
    fleets = db.relationship("Fleet", backref='admiral', lazy='dynamic')
    sorties = db.relationship("AdmiralSortie", backref='admiral', lazy='dynamic')
    quests = db.relationship("AdmiralQuest", backref='admiral', lazy='dynamic')

    # If this is false...
    # 1) api_req_init is enabled
    #   2) setup() is enabled, which means a new fleet will be automatically added, and two docks of each kind
    # If this is true...
    #   1) api_req_init will be disabled
    #   2) setup() is disabled.
    setup = db.Column(db.Boolean())
    docks = db.relationship("Dock", backref='admiral', lazy='dynamic', order_by='Dock.id')

    items = db.relationship("AdmiralItem", lazy="dynamic")

    lastaction = db.Column(db.DateTime)

    def __str__(self):
        return "Admiral " + self.user.nickname

class Stats(db.Model):
    """
    Because we must protect out sanity.

    About defaults: this creates and awkward situation where, for instance, Items have hp.
    This will not have any consequences unless you decide that if an Item has hp, it must be a Ship.
    The alternative would be leaving it None, but whenever you create a new Ship you'd have to set that all manually.
    That would be a bother, so let's not go crazy out there, huh?
    """
    id = db.Column(db.Integer, primary_key=True)

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
    los = db.Column(db.Integer, default=0)
    hp = db.Column(db.Integer,default=1)

    #Probably worth including it here
    ammo = db.Column(db.Integer)
    fuel = db.Column(db.Integer)

class AdmiralShip(db.Model):
    id = db.Column(db.Integer, primary_key=True)   

    local_fleet_num = db.Column(db.Integer)
    local_ship_num = db.Column(db.Integer, nullable=False)
    
    fatigue = db.Column(db.Integer, default=49)

    exp = db.Column(db.Integer)
    level = db.Column(db.Integer)
    repair_base = db.Column(db.String())
    
    heartlocked = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=False, nullable=False)

    admiral_id = db.Column(db.Integer, db.ForeignKey('admiral.id'))    
    ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'))
    fleet_id = db.Column(db.Integer, db.ForeignKey('fleet.id'))
    stats_id = db.Column(db.Integer, db.ForeignKey('stats.id'))

    ship = db.relationship("Ship", uselist=False)    
    items = db.relationship("AdmiralShipItem",order_by='AdmiralShipItem.slot')
    stats = db.relationship("Stats")

    def __str__(self):
        return self.ship.name



class AdmiralQuest(db.Model):
    """
    progress: None,50,80
    state: Inactive, Active, Complete
    """
    id = db.Column(db.Integer, primary_key=True)
    admiral_id = db.Column(db.Integer, db.ForeignKey('admiral.id'))
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'))

    progress = db.Column(db.Integer, default=QUEST_PROGRESS_0)
    state = db.Column(db.Integer, default=QUEST_STATE_INACTIVE)
    data = db.Column(db.String(255),default='')

    quest = db.relationship("Quest")

class AdmiralSortie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admiral_id = db.Column(db.Integer, db.ForeignKey('admiral.id'))
    sortie_id = db.Column(db.Integer, db.ForeignKey('sortie.id'))
    cleared = db.Column(db.Integer,default=0)
    defeat_count = db.Column(db.Integer)

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    #Must mirror api_data2 for modernization porposes, or we'd have to do it manually
    api_id = db.Column(db.Integer)
    
    remodel = db.Column(db.Integer, nullable=True)    
    remodel_level = db.Column(db.Integer, nullable=True)

    rarity = db.Column(db.Integer)    

    name = db.Column(db.String)
    number = db.Column(db.Integer)
    stype = db.Column(db.Integer)

    voicef = db.Column(db.Integer)    

    modern_use = db.Column(db.String)
    srange = db.Column(db.Integer, default=0)

    kai = db.Column(db.Boolean, default=False)

    id_remodel_cost = db.Column(db.Integer, db.ForeignKey('resource.id'))
    id_broken = db.Column(db.Integer, db.ForeignKey('resource.id'))
    id_stats =db.Column(db.Integer, db.ForeignKey('stats.id'))
    id_max_stats = db.Column(db.Integer, db.ForeignKey('stats.id'))
    
    remodel_cost = db.relationship("Resource",foreign_keys='Ship.id_remodel_cost')
    broken = db.relationship("Resource",foreign_keys='Ship.id_broken')
    stats = db.relationship("Stats",foreign_keys='Ship.id_stats')
    max_stats = db.relationship("Stats",foreign_keys='Ship.id_max_stats')

    # Messages
    getmsg = db.Column(db.Text())
    buildtime = db.Column(db.Integer)

    maxslots = db.Column(db.Integer())
    maxplanes = db.Column(db.Integer())

    def __str__(self):
        return self.name

class Recipe(db.Model):
    __tablename__ = 'recipe'
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

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # I'm pretty sure we have to have a field to mirror the Item api_id from api_data2.
    # I might be wrong. My head hurts.
    api_id = db.Column(db.Integer,default=0) 
    rarity = db.Column(db.Integer,default=0)
    info = db.Column(db.String(255))
    usebull = db.Column(db.String(1))
    sortno = db.Column(db.Integer)
    name = db.Column(db.String(255))
    types = db.Column(db.String(50))

    id_broken = db.Column(db.Integer, db.ForeignKey('resource.id'))
    id_stats = db.Column(db.Integer, db.ForeignKey('stats.id'))    

    stats = db.relationship("Stats")
    broken = db.relationship("Resource")

class ItemType(db.Model):
    """
    Table of slottypes. Not necessary, but we should use this for efficiency.
    The alternative would be a column on type with an String and eval it.

    Currently not being used, but I'll leave this here to when I find out what slottypes actually does.
    """
    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.Integer)

class Resource(db.Model):
    """
    Because parsing strings suck.
    """
    id = db.Column(db.Integer,primary_key=True)
    fuel = db.Column(db.Integer,default=0)
    ammo = db.Column(db.Integer,default=0)
    steel = db.Column(db.Integer,default=0)
    baux = db.Column(db.Integer,default=0)

    flame = db.Column(db.Integer,default=0)
    bucket = db.Column(db.Integer,default=0)
    material = db.Column(db.Integer,default=0)

    def to_list(self):
        data = []
        if resource.fuel is not None: data.append(resource.fuel)
        if resource.ammo is not None: data.append(resource.ammo)
        if resource.steel is not None: data.append(resource.steel)
        if resource.baux is not None: data.append(resource.baux)
    
        if resource.flame is not None: data.append(resource.flame)
        if resource.bucket is not None: data.append(resource.bucket)
        if resource.material is not None: data.append(resource.material)
        return data

class AdmiralItem(db.Model):
    """
    There's a lot of guessing going on in all of this Item modeling...
    """
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer,default=0)
    locked = db.Column(db.Integer,default=0)

    admiral_id = db.Column(db.Integer, db.ForeignKey("admiral.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))

class AdmiralShipItem(db.Model):
    """
    admiral_item_id: When None, you must set it to -1 when responding to Kancolle.
    """
    id = db.Column(db.Integer, primary_key=True)
    slot = db.Column(db.Integer)
    admiral_ship_id = db.Column(db.Integer, db.ForeignKey("admiral_ship.id"))
    admiral_item_id = db.Column(db.Integer, db.ForeignKey("admiral_item.id"))

class Sortie(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    is_boss = db.Column(db.Integer, default=0)
    level = db.Column(db.String(10))

class Quest(db.Model):
    """
    no: the Quest id, so use that when it asks for no. I'll leave this here just in case
    frequency: Once,Daily,Weekly. Kancolle calls this 'type'
    category: Compostition, Exercise, etc.
    bonus_flag: ?
    invalid_flag: ?
    reward = resources reward
    code: A1,B20, etc. Used to make it easier to track quest progress
    """
    id = db.Column(db.Integer,primary_key=True)

    no = db.Column(db.Integer)
    category = db.Column(db.Integer)
    frequency = db.Column(db.Integer)
    title = db.Column(db.String(255))
    detail = db.Column(db.Text)
    bonus_flag = db.Column(db.Integer)
    invalid_flag = db.Column(db.Integer)    
    code = db.Column(db.String(3))

    resource_id = db.Column(db.Integer,db.ForeignKey("resource.id"))

    reward = db.relationship("Resource")
    bonuses = db.relationship("QuestBonus")

class QuestRequirement(db.Model):
    """
    Every time an Admiral completes a Quest, it may have uncloked new Quests, but a Quest may have more than one Quest as requirement, so the process goes:
    Completes Quest X -> list all entries that have quest X as required_id -> foreach entry, verify if admiral has AdmiralQuest.quest_id = required_id

    There are other approaches to this, so we might have to review depending on efficiency.
    """
    id = db.Column(db.Integer,primary_key=True)
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'))
    required_id = db.Column(db.Integer,db.ForeignKey('quest.id'))

class QuestBonus(db.Model):
    """
    kind: Kancolle calls this 'type'.
    It probably indicates if bonus is extra fleet, item, or whatever. Testing needed.
    """
    id = db.Column(db.Integer,primary_key=True)    
    kind = db.Column(db.Integer)    
    quantity = db.Column(db.Integer)
    quest_id = db.Column(db.Integer, db.ForeignKey("quest.id"))

    item_id = db.Column(db.Integer, db.ForeignKey("item.id"))
    ship_id = db.Column(db.Integer, db.ForeignKey("ship.id"))
    
    quest = db.relationship("Quest")
    item = db.relationship("Item")
    ship = db.relationship("Ship")    

role__user = db.Table('role__user',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                      )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean)

    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    confirmed_at = db.Column(db.DateTime())

    nickname = db.Column(db.String(255), unique=True, nullable=False)
    api_token = db.Column(db.String(40), default=lambda: generate_api_token(), unique=True)

    admiral = db.relationship("Admiral", backref='user', uselist=False)

    roles = db.relationship('Role', secondary=role__user, backref=db.backref('users', lazy='dynamic'))  # Fix roles

    def __str__(self):
        return self.email

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)

    def __str__(self):
        return self.name