from . import db

class Kanmusu(db.Model):
    __tablename__ = 'kanmusu'

    id = db.Column(db.Integer, primary_key=True)
    fleet_position = db.Column(db.Integer)
    number = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer)
    experience = db.Column(db.Integer)
    current_hp = db.Column(db.Integer)
    current_fuel = db.Column(db.Integer)
    current_ammo = db.Column(db.Integer)
    fatigue = db.Column(db.Integer)
    locked = db.Column(db.Boolean)
    active = db.Column(db.Boolean, nullable=False)
    admiral_id = db.Column(db.ForeignKey('admiral.id'))
    ship_id = db.Column(db.ForeignKey('ship.id'))
    fleet_id = db.Column(db.ForeignKey('fleet.id'))
    stats_id = db.Column(db.ForeignKey('stats.id'), index=True)
    
    ship = db.relationship('Ship')
    stats = db.relationship('Stats')


class KanmusuEquipment(db.Model):
    __tablename__ = 'kanmusu_equipment'

    id = db.Column(db.Integer, primary_key=True)
    slot = db.Column(db.Integer)
    kanmusu_id = db.Column(db.ForeignKey('kanmusu.id'))
    admiral_equipment_id = db.Column(db.ForeignKey('admiral_equipment.id'))

    admiral_equipment = db.relationship('AdmiralEquipment')
    kanmusu = db.relationship('Kanmusu')



class Remodel(db.Model):
    __tablename__ = 'remodel'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    remodel_api_id = db.Column(db.Integer)
    id_resources = db.Column(db.ForeignKey('resources.id'), index=True)

    cost = db.relationship('Resources')


class Ship(db.Model):
    __tablename__ = 'ship'

    id = db.Column(db.Integer, primary_key=True)
    api_id = db.Column(db.Integer)
    name = db.Column(db.String)
    number = db.Column(db.Integer)
    rarity = db.Column(db.Integer)
    type_ = db.Column(db.Integer)
    voicef = db.Column(db.Integer)
    slots = db.Column(db.Integer)
    kai = db.Column(db.Boolean)
    getmsg = db.Column(db.Text)
    buildtime = db.Column(db.Integer)
    maxslots = db.Column(db.Integer)
    maxplanes = db.Column(db.String)
    max_stats_id = db.Column(db.ForeignKey('stats.id'), index=True)
    base_stats_id = db.Column(db.ForeignKey('stats.id'), index=True)
    broken_resources_id = db.Column(db.ForeignKey('resources.id'), index=True)
    modern_resources_id = db.Column(db.ForeignKey('resources.id'), index=True)
    remodel_id = db.Column(db.ForeignKey('remodel.id'), unique=True)

    base_stats = db.relationship('Stats', primaryjoin='Ship.base_stats_id == Stats.id')
    dismantling = db.relationship('Resources', primaryjoin='Ship.broken_resources_id == Resources.id')
    max_stats = db.relationship('Stats', primaryjoin='Ship.max_stats_id == Stats.id')
    modernization = db.relationship('Resources', primaryjoin='Ship.modern_resources_id == Resources.id')
    remodel = db.relationship('Remodel', uselist=False)

#from . import Fleet


