import db
import util

def get_ship_from_recipe(fuel=30, ammo=30, steel=30, baux=30):
    admiral = util.get_token_admiral_or_error()
    if admiral.user.nickname == "upfinnarn":
        # Naka-chan is shit.
        return 56
    ships = db.Recipe.query.filter((db.Recipe.minfuel >= fuel) & (db.Recipe.maxfuel <= fuel)) \
        .filter((db.Recipe.minammo >= ammo) & (db.Recipe.maxammo <= ammo)) \
        .filter((db.Recipe.minsteel >= steel) & (db.Recipe.maxsteel <= steel)) \
        .filter((db.Recipe.minbaux >= baux) & (db.Recipe.maxsteel <= baux))


def generate_dock_data(admiral_obj: db.Admiral=None, admiralid: int=None) -> dict:
    """
    Generates dock data.
    :param admiral: Generate from this db.Admiral instance.
    :param admiralid: Generate from this admiral ID.
    :return: A dict containing the dock data. d['rdock'] for repair docks, d['cdock'] for crafting docks
    """
    # TODO: Refactor and make this nicer.
    if admiral_obj:
        admiral = admiral_obj
    elif admiralid:
        admiral = db.Admiral.query.filter_by(id=admiralid)
    ob = {"rdock": [], "cdock": []}
    for x in range(0, 4):
        if admiral.available_cdocks - 1 >= x:
            dock = admiral.crafting_docks.all()[x]
            ob['cdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': dock.state,
                                'api_created_ship_id': dock.ship,
                                'api_complete_time': dock.complete,
                                'api_complete_time_str': dock.complete.strftime('%Y-%M-%d %H:%M:%S'),
                                'api_item1': dock.fuel,
                                'api_item2': dock.ammo,
                                'api_item3': dock.steel,
                                'api_item4': dock.baux,
                                'api_item5': dock.cmats
                                })
        else:
            ob['cdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': -1,
                                'api_created_ship_id': 0,
                                'api_complete_time': 0,
                                'api_complete_time_str': "",
                                'api_item1': 0,
                                'api_item2': 0,
                                'api_item3': 0,
                                'api_item4': 0,
                                'api_item5': 0
                                })
    for x in range(0, 4):
        if admiral.available_rdocks - 1 >= x:
            dock = admiral.repair_docks.all()[x]
            ob['rdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': dock.state,
                                'api_created_ship_id': dock.ship,
                                'api_complete_time': dock.complete,
                                'api_complete_time_str': dock.complete.strftime('%Y-%M-%d %H:%M:%S'),
                                'api_item1': dock.fuel,
                                'api_item2': dock.ammo,
                                'api_item3': dock.steel,
                                'api_item4': dock.baux,
                                'api_item5': dock.cmats
                                })
        else:
            ob['rdock'].append({'api_member_id': admiral.id,
                                'api_id': x,
                                'api_state': -1,
                                'api_created_ship_id': 0,
                                'api_complete_time': 0,
                                'api_complete_time_str': "",
                                'api_item1': 0,
                                'api_item2': 0,
                                'api_item3': 0,
                                'api_item4': 0,
                                'api_item5': 0
                                })
    return ob
