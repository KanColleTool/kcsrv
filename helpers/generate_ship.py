import db


def get_repair_base(original_ship):
    return "0,0,0,0"


def generate_new_ship(shipid):
    original_ship = db.Ship.query.filter_by(id=shipid).first()
    assert isinstance(original_ship, db.Ship)
    if not original_ship: return
    admiral_ship = db.AdmiralShip(
        ship = original_ship,
        ammo = original_ship.ammo_max,
        fuel = original_ship.fuel_max,
        exp = 0,
        level = 1,
        repair_base = get_repair_base(original_ship),
        luck = original_ship.luck_base,
        luck_eq = original_ship.luck_base,
        firepower = original_ship.firepower_base,
        firepower_eq = original_ship.firepower_base,
        armour = original_ship.armour_base,
        torpedo = original_ship.torpedo_base,
        torpedo_eq = original_ship.torpedo_base,
        antiair = original_ship.antiair_base,
        antiair_eq = original_ship.antiair_base,
        antisub = original_ship.antisub_base,
        evasion = original_ship.evasion_base,
        fatigue = 49,
        current_hp = original_ship.hp_base
    )
    return admiral_ship