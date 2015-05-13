import db


def get_ship_from_recipe(fuel=30, ammo=30, steel=30, baux=30):
    ships = db.Recipe.query.filter((db.Recipe.minfuel >= fuel) & (db.Recipe.maxfuel <= fuel)) \
        .filter((db.Recipe.minammo >= ammo) & (db.Recipe.maxammo <= ammo)) \
        .filter((db.Recipe.minsteel >= steel) & (db.Recipe.maxsteel <= steel)) \
        .filter((db.Recipe.minbaux >= baux) & (db.Recipe.maxsteel <= baux))