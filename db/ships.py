from . import db,Stats
from sqlalchemy import inspect

class Kanmusu(db.Model):
    __tablename__ = 'kanmusu'

    id = db.Column(db.Integer, primary_key=True)
    fleet_position = db.Column(db.Integer)
    number = db.Column(db.Integer, nullable=False)
    level = db.Column(db.Integer, default=1)
    experience = db.Column(db.Integer, default=0)
    current_hp = db.Column(db.Integer, default=1)
    current_fuel = db.Column(db.Integer, default=0)
    current_ammo = db.Column(db.Integer, default=0)
    fatigue = db.Column(db.Integer, default=49)
    locked = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True, nullable=False)

    admiral_id = db.Column(db.ForeignKey('admiral.id'))
    ship_id = db.Column(db.ForeignKey('ship.id'))
    fleet_id = db.Column(db.ForeignKey('fleet.id'))
    stats_id = db.Column(db.ForeignKey('stats.id'), index=True)
    modern_stats_id = db.Column(db.ForeignKey('stats.id'), index=True)

    equipments = db.relationship('KanmusuEquipment',order_by="KanmusuEquipment.slot")
    ship = db.relationship('Ship')
    stats = db.relationship('Stats', foreign_keys="Kanmusu.stats_id")
    modernized_stats = db.relationship('Stats', foreign_keys="Kanmusu.modern_stats_id")

    def create(self, ship_id=None, ship_api_id=None):
        ship = Ship.get(id=ship_id, ship_api_id=ship_api_id)
        self.ship = ship
        self.base_stats = ship.base_stats.copy()
        self.stats = ship.base_stats.copy()
        self.current_ammo = self.stats.ammo
        self.current_fuel = self.stats.fuel
        self.current_hp = self.stats.hp
        self.equipments = [KanmusuEquipment(slot=i) for i in range(ship.maxslots)]
        self.modernized_stats = Stats(firepower=0,torpedo=0,antiair=0,armour=0,luck=0)
        return self

    @staticmethod
    def get(id):
        return db.session.query(Kanmusu).get(id)

    def equip(self,slot,admiral_equip_id=None):
        """
        Replace a Kanmusu equipment
        :param slot: The slot which make the operation
        :param admiral_equip_id: The ID of an AdmiralEquipment entry.
        """
        if int(admiral_equip_id) == -1:
            admiral_equip_id = None
        else:
            new_stats = self.admiral.get_equipment(admiral_equip_id).equipment.stats
            self.stats.add(new_stats)

        if self.equipments[int(slot)].admiral_equipment_id is not None:
            old_stats = self.equipments[int(slot)].admiral_equipment.equipment.stats
            self.stats.sub(old_stats)

        self.equipments[int(slot)].admiral_equipment_id = admiral_equip_id
        db.session.add(self)

    def modernize(self,id_list):
        """
        Modernize a Kanmusu
        :param id_list: A list of Kanmusu IDs
        :rtype Boolean
        :return: Modernization success?
        """
        for id in id_list:
            #TODO Modernization logic
            food = Kanmusu.get(id)
            self.stats.add(food.ship.modernization)
            self.modernized_stats.add(food.ship.modernization)
            db.session.delete(food)
        self.validate_stats()
        db.session.add(self)
        return True

    def validate_stats(self):
        """
        Making sure all stats are within range.
        We'll remove all gear, verify if they are less than max, adjust if needed, add all gear again.
        This almost convinced me to make a base_stats for Kanmusu.
        Almost.
        """
        temp_equip = []
        for n in range(self.ship.maxslots):
            temp_equip.append(self.equipments[n].admiral_equipment_id)
            self.equip(n,-1)
        mapper = inspect(self.stats)
        for column in mapper.attrs:
            current_value = getattr(self.stats, column.key)
            max_value = getattr(self.ship.max_stats, column.key)
            if column.key != "id" and current_value is not None and max_value is not None:
                if current_value > max_value:
                    setattr(self.stats,column,max_value)
        for n in range(self.ship.maxslots):
            aequip_id = temp_equip[n] if temp_equip[n] else -1
            self.equip(n,aequip_id)
        #This is exactly my idea of efficient method that doesn't look redundant at all!

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
    modern_stats_id = db.Column(db.ForeignKey('stats.id'), index=True)
    remodel_id = db.Column(db.ForeignKey('remodel.id'), unique=True)

    # TODO: Distinction between base_stats/max_stats needs to be made more clear.
    # If you're wondering, it's found in `offline/dbpopulate:ships()`.

    base_stats = db.relationship('Stats', primaryjoin='Ship.base_stats_id == Stats.id')
    dismantling = db.relationship('Resources', primaryjoin='Ship.broken_resources_id == Resources.id')
    max_stats = db.relationship('Stats', primaryjoin='Ship.max_stats_id == Stats.id')
    modernization = db.relationship('Stats', primaryjoin='Ship.modern_stats_id == Stats.id')
    remodel = db.relationship('Remodel', uselist=False)

    @staticmethod
    def get(id=None, ship_api_id=None):
        """
        Gets a ship.
        :param id: The Ship internal ID to get.
        :param ship_api_id: The Ship API id to get.
        :rtype Ship
        :return: A new ship object.
        """
        if id:
            return db.session.query(Ship).get(id)
        elif ship_api_id:
            return Ship.query.filter(Ship.api_id == ship_api_id).first()
        else:
            return None
