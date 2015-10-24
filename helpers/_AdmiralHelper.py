# from db import db,User,Admiral,Dock,AdmiralQuest,Resource,AdmiralItem


"""These are API version 1 functions only."""


#def basic():
#    admiral = g.admiral
#    """
#    Gets the basic info for the admiral.
#    :return: A dict containing the KanColle info for the admiral.
#    """




"""
def get_admiral_furniture():
    return [int(x) for x in util.get_token_admiral_or_error().furniture.split(',')]

def get_admiral_sorties():
    
    Gets Admiral's unlocked Sorties
    :return: A list containing dicts of KanColle Sortie info for the Admiral
    
    admiral = util.get_token_admiral_or_error()
    data = []
    for admiral_sortie in admiral.sorties.all():
        sortie = db.Sortie.query.filter_by(id=admiral_sortie.sortie_id).first()
        data.append({
            'api_id': sortie.level,
            'api_cleared': admiral_sortie.cleared,
            'api_exboss_flag': sortie.is_boss,
            'api_defeat_count': admiral_sortie.defeat_count #Unnecessary if is not boss
        })
    return data

def get_admiral_v2(api_token: str):    
    user = User.query.filter_by(api_token=api_token).first()
    if not user:
        return None
    if not user.admiral:
        adm = db.Admiral()
        user.admiral = adm
        db.session.add(user)
        db.session.commit()
    return user.admiral

def get_admiral_v2_from_id_or_token(search: object):

    if len(search) == 40:
        user = User.query.filter_by(api_token=search).first()
    elif search:
        user = User.query.filter_by(id=search).first()
    else:
        return None
    if not user:
        return None
    if not user.admiral:
        adm = db.Admiral()
        user.admiral = adm
        db.session.add(user)
        db.session.commit()
    return user.admiral



def get_admiral_deck_api_data(admiral):
    count = 0
    # Fleets.    
    fleet_api_data = []
    for fleet in admiral.fleets.all():
        count += 1
        ships = [ship.local_ship_num+1 for ship in fleet.ships.all() if ship is not None]
        fleet_api_data.append({
            # Unknown value, always zero for some reason.
            'api_flagship': 0,
            # The Admiral ID, presumably.
            'api_member_id': admiral.id,
            # The name of the fleet.
            'api_name': fleet.name,
            # Unknown value, always empty.
            'api_name_id': "",
            # The local fleet ID.
            'api_id': count,
            # List of ships.
            "api_ship": ships + [-1] * (6 - len(ships)),
            # Mission data?
            "api_mission": [0, 0, 0, 0]
        })
    return fleet_api_data

def get_admiral_resources_api_data(admiral):
    resources = admiral.resources.to_list()
    data = [{
        "api_id": n + 1,
        "api_member_id": admiral.id,
        "api_value": resource
    } for n,resource in enumerate(resources)]
    # I have no idea what this is, it can have any api_value
    # but without it flame/bucket/mat always show up as 0.
    data.append({"api_id": 8,"api_member_id": admiral.id,"api_value":1})
    return data


def admiral_grant_resources(admiral,resource=None,**kwargs):
    admiral.resources = ResourceHelper.update_resource(admiral.resources,resource,kwargs)
    db.session.add(admiral)
    db.session.commit()

def admiral_grant_item(admiral,item_id,quantity=1):
    for _ in range(quantity):
        db.session.add(AdmiralItem(admiral_id=admiral.id,item_id=item_id))
    db.session.commit()

def admiral_grant_ship(admiral,ship_id=None,ship_api_id=None,quantity=1):
    for _ in range(quantity):
        admiral.admiral_ships.append(ShipHelper.get_new_admiral_ship(admiral,ship_id,ship_api_id))
    db.session.add(admiral)
    db.session.commit()
"""
