from . import db

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

    admiral_ship_id = db.Column(db.Integer, db.ForeignKey("admiral_ship.id"))

    name = db.Column(db.String(255), primary_key=True)
    desc = db.Column(db.Text)

    usable = db.Column(db.Boolean, default=False)

    increase_fp = db.Column(db.Boolean)
    increase_aa = db.Column(db.Boolean)
    increase_tp = db.Column(db.Boolean)
    increase_ar = db.Column(db.Boolean)

    increase_amount = db.Column(db.Integer, nullable=False)

    rarity = db.Column(db.Integer, nullable=False)

    sortno = db.Column(db.Integer)