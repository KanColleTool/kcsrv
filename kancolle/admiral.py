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

    admiral_ships = db.relationship("AdmiralShip", backref='admiral', lazy='dynamic')

    resources = db.Column(db.String())

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

    lastaction = db.Column(db.DateTime)

    def __str__(self):
        return "Admiral " + self.user.nickname

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

    items = db.relationship("Item", backref="admiral_ship", lazy="dynamic")

    def __str__(self):
        return self.ship.name



class AdmiralQuest(db.Model):
    """
    progress: None,50,80
    state: Inactive, Active, Complete
    """
    admiral_id = db.Column(db.Integer, db.ForeignKey('admiral.id'),primary_key=True)
    quest_id = db.Column(db.Integer, db.ForeignKey('quest.id'),primary_key=True)

    progress = db.Column(db.Integer)
    state = db.Column(db.Integer)

class AdmiralSortie(db.Model):
    admiral_id = db.Column(db.Integer, db.ForeignKey('admiral.id'),primary_key=True)
    sortie_id = db.Column(db.Integer, db.ForeignKey('sortie.id'),primary_key=True)
    cleared = db.Column(db.Integer,default=0)
    defeat_count = db.Column(db.Integer)   