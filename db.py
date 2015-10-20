from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import UserMixin, RoleMixin
from sqlalchemy import inspect
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

"""
Stats are a Ship intrinsic attributes. She has 30 firepower. She has 40 hp.
Current hp, fuel, ammo are stored in AdmiralShip table.
"""

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    luck = db.Column(db.Integer, default=0)    
    firepower = db.Column(db.Integer, default=0)    
    armour = db.Column(db.Integer, default=0)
    torpedo = db.Column(db.Integer, default=0)    
    antiair = db.Column(db.Integer, default=0)    
    antisub = db.Column(db.Integer, default=0)
    evasion = db.Column(db.Integer, default=0)
    los = db.Column(db.Integer, default=0)
    srange = db.Column(db.Integer,default=0)

    hp = db.Column(db.Integer)
    ammo = db.Column(db.Integer)
    fuel = db.Column(db.Integer)

    def copy(self,target=None):        
        target = target if target else Stats()
        id = target.id
        for c in inspect(Stats).c:
            setattr(target, c.name, getattr(self, c.name))
        target.id = id
        return target

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

    itemslots = db.Column(db.Integer)

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
    getmsg = db.Column(db.Text())
    buildtime = db.Column(db.Integer)

    maxslots = db.Column(db.Integer())
    maxplanes = db.Column(db.String())

    def __str__(self):
        return self.name
"""
    repair_base_id = db.Column(db.Integer,db.ForeignKey('resource.id'))
    remodel_cost_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    broken_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    
    
    remodel_cost = db.relationship("Resource",foreign_keys='Ship.remodel_cost_id')
    broken = db.relationship("Resource",foreign_keys='Ship.broken_id')
    # There's no repair base on api_data2, we'll have to do it manually...
    repair_base = db.relationship("Resource",foreign_keys='Ship.repair_base_id')


    modernization = db.relationship("Stats",foreign_keys='Ship.modernization_id')
    stats = db.relationship("Stats",foreign_keys='Ship.stats_id')
    stats_max = db.relationship("Stats",foreign_keys='Ship.stats_max_id')
    modernization_id = db.Column(db.Integer, db.ForeignKey('stats.id'))
    stats_id =db.Column(db.Integer, db.ForeignKey('stats.id'))
    stats_max_id = db.Column(db.Integer, db.ForeignKey('stats.id'))
""" 

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
    items = db.relationship("AdmiralShipItem",order_by='AdmiralShipItem.slot')
    """
    stats = db.relationship("Stats")
    stats_id = db.Column(db.Integer, db.ForeignKey('stats.id'))
    """
    def __str__(self):
        return self.ship.name

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
    sortno = db.Column(db.Integer)
    api_id = db.Column(db.Integer)
    info = db.Column(db.String())
    usebull = db.Column(db.String())
    name = db.Column(db.String())
    rarity = db.Column(db.String())
    broken = db.Column(db.String())
    types = db.Column(db.String())
    taik = db.Column(db.Integer,default=0)
    souk = db.Column(db.Integer,default=0)
    houg = db.Column(db.Integer,default=0)
    raig = db.Column(db.Integer,default=0)
    soku = db.Column(db.Integer,default=0)
    baku = db.Column(db.Integer,default=0)
    tyku = db.Column(db.Integer,default=0)
    tais = db.Column(db.Integer,default=0)
    atap = db.Column(db.Integer,default=0)
    houm = db.Column(db.Integer,default=0)
    raim = db.Column(db.Integer,default=0)
    houk = db.Column(db.Integer,default=0)
    raik = db.Column(db.Integer,default=0)
    bakk = db.Column(db.Integer,default=0)
    saku = db.Column(db.Integer,default=0)
    sakb = db.Column(db.Integer,default=0)
    luck = db.Column(db.Integer,default=0)
    leng = db.Column(db.Integer,default=0)

    """
    broken_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    stats_id = db.Column(db.Integer, db.ForeignKey('stats.id'))    

    stats = db.relationship("Stats")
    broken = db.relationship("Resource")
    """

class Resource(db.Model):
    """
    Because parsing strings suck.
    """
    id = db.Column(db.Integer,primary_key=True)
    fuel = db.Column(db.Integer)
    ammo = db.Column(db.Integer)
    steel = db.Column(db.Integer)
    baux = db.Column(db.Integer)

    flame = db.Column(db.Integer)
    bucket = db.Column(db.Integer)
    material = db.Column(db.Integer)

    def to_list(self):
        data = []
        if self.fuel is not None: data.append(self.fuel)
        if self.ammo is not None: data.append(self.ammo)
        if self.steel is not None: data.append(self.steel)
        if self.baux is not None: data.append(self.baux)
    
        if self.flame is not None: data.append(self.flame)
        if self.bucket is not None: data.append(self.bucket)
        if self.material is not None: data.append(self.material)
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
    bonuses = db.relationship("QuestBonus", lazy='dynamic', foreign_keys="QuestBonus.quest_id")

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