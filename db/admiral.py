from constants import *
from . import db
from db.support import Resources


class Admiral(db.Model):
    __tablename__ = 'admiral'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('admiral_id_seq'::regclass)")
    name = db.Column(db.String(100))
    level = db.Column(db.Integer,default=1)
    experience = db.Column(db.Integer,default=0)
    rank = db.Column(db.Integer,default=8)

    furniture_coins = db.Column(db.Integer,default=1)

    max_kanmusu = db.Column(db.Integer,default=5000)
    max_equipment = db.Column(db.Integer,default=10000)
    max_furniture = db.Column(db.Integer,default=10000)

    sortie_total = db.Column(db.Integer,default=0)
    sortie_successes = db.Column(db.Integer,default=0)
    expedition_total = db.Column(db.Integer,default=0)
    expedition_successes = db.Column(db.Integer,default=0)
    pvp_total = db.Column(db.Integer,default=0)
    pvp_successes = db.Column(db.Integer,default=0)

    tutorial_progress = db.Column(db.Integer,default=0)
    last_action = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)

    resources_id = db.Column(db.ForeignKey('resources.id'))
    user_id = db.Column(db.ForeignKey('user.id'))

    kanmusu = db.relationship('Kanmusu')
    resources = db.relationship('Resources')
    fleets = db.relationship('Fleet')
    docks_craft = db.relationship("Dock",
                                  primaryjoin="and_(Admiral.id==Dock.admiral_id," +\
                                              "Dock.type_==" + str(DOCK_TYPE_CRAFT) +")",
                                  lazy='dynamic', order_by='Dock.number')
    docks_repair = db.relationship("Dock",
                                   primaryjoin="and_(Admiral.id==Dock.admiral_id," +\
                                               "Dock.type_==" + str(DOCK_TYPE_REPAIR) +")",
                                  lazy='dynamic', order_by='Dock.number')

    def create(self, user):
        self.resources = Resources(fuel=500, ammo=500, steel=500, baux=500)
        self.docks_craft = [Dock(type_=DOCK_TYPE_CRAFT, number=n + 1) for n in range(3)]
        self.docks_repair = [Dock(type_=DOCK_TYPE_REPAIR, number=n + 1) for n in range(3)]
        self.fleets = [Fleet(number=0)]
        """
        last = user.admiral.lastaction
        if last is None:
            last = datetime.datetime.utcnow()
        now = datetime.datetime.utcnow()

        # convert to unix timestamp
        d1_ts = time.mktime(now.timetuple())
        d2_ts = time.mktime(last.timetuple())

        minutes = math.floor(int(d1_ts-d2_ts) / 60)

        resources = user.admiral.resources.to_list()
        if minutes != 0:
            for n, val in enumerate(resources):
                if n >= 4:
                    break
                resources[n] += (3 * minutes) if n != 3 else minutes
            user.admiral.resources = pack_resources(resources)
            user.admiral.lastaction = datetime.datetime.utcnow()
        """
        user.admiral = self
        db.session.add(user)
        db.session.commit()
        return self


class AdmiralEquipment(db.Model):
    __tablename__ = 'admiral_equipment'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('admiral_equipment_id_seq'::regclass)")
    level = db.Column(db.Integer)
    locked = db.Column(db.Integer)
    admiral_id = db.Column(db.ForeignKey('admiral.id'))
    equipment_id = db.Column(db.ForeignKey('equipment.id'))

    admiral = db.relationship('Admiral')
    equipment = db.relationship('Equipment')


class AdmiralFurniture(db.Model):
    __tablename__ = 'admiral_furniture'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('admiral_furniture_id_seq'::regclass)")
    active = db.Column(db.Boolean)
    admiral_id = db.Column(db.ForeignKey('admiral.id'), index=True)
    furniture_id = db.Column(db.ForeignKey('furniture.id'), index=True)

    admiral = db.relationship('Admiral')
    furniture = db.relationship('Furniture')


class AdmiralItem(db.Model):
    __tablename__ = 'admiral_item'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('admiral_item_id_seq'::regclass)")
    admiral_id = db.Column(db.ForeignKey('admiral.id'), index=True)
    item_id = db.Column(db.ForeignKey('item.id'), index=True)

    admiral = db.relationship('Admiral')
    item = db.relationship('Item')


class AdmiralQuest(db.Model):
    __tablename__ = 'admiral_quest'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('admiral_quest_id_seq'::regclass)")
    progress = db.Column(db.Integer)
    state = db.Column(db.Integer)
    data = db.Column(db.String(255))
    admiral_id = db.Column(db.ForeignKey('admiral.id'))
    quest_id = db.Column(db.ForeignKey('quest.id'))

    admiral = db.relationship('Admiral')
    quest = db.relationship('Quest')


class Dock(db.Model):
    __tablename__ = 'dock'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('dock_id_seq'::regclass)")
    number = db.Column(db.Integer)
    type_ = db.Column(db.Integer)
    state = db.Column(db.Integer)
    complete = db.Column(db.BigInteger)
    admiral_id = db.Column(db.ForeignKey('admiral.id'))
    kanmusu_id = db.Column(db.ForeignKey('kanmusu.id'))
    resources_id = db.Column(db.ForeignKey('resources.id'), index=True)

    resources = db.relationship('Resources')
    kanmusu = db.relationship('Kanmusu')


class Fleet(db.Model):
    __tablename__ = 'fleet'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('fleet_id_seq'::regclass)")
    name = db.Column(db.String,name="Unnamed")
    number = db.Column(db.Integer)
    admiral_id = db.Column(db.ForeignKey('admiral.id'))

    admiral = db.relationship('Admiral')
