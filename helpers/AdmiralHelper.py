import util,datetime,time,math
from db import db,User,Admiral,Dock,AdmiralQuest,Resource
from . import ResourceHelper
"""These are API version 1 functions only."""

def get_admiral_furniture():
    return [int(x) for x in util.get_token_admiral_or_error().furniture.split(',')]

def get_admiral_basic_info():
    """
    Gets the basic info for the admiral.
    :return: A dict containing the KanColle info for the admiral.
    """
    admiral = util.get_token_admiral_or_error()
    return {
        'api_member_id': admiral.id,
        'api_nickname': admiral.user.nickname,
        'api_nickname_id': admiral.user.id,
        'api_active_flag': 1,
        'api_starttime': 1430603452688,
        'api_level': admiral.level,
        'api_rank': admiral.rank,
        'api_experience': admiral.experience,
        'api_fleetname': None,
        'api_comment': "",
        'api_comment_id': "",
        'api_max_chara': admiral.max_ships,
        'api_max_slotitem': admiral.max_equips,
        'api_max_kagu': admiral.max_furniture,
        'api_playtime': 0,
        'api_tutorial': 0,
        'api_furniture': [int(x) for x in admiral.furniture.split(',')],
        'api_count_deck': admiral.available_fleets,
        'api_count_kdock': admiral.available_cdocks,
        'api_count_ndock': admiral.available_rdocks,
        'api_fcoin': admiral.furniture_coins,
        'api_st_win': admiral.sortie_successes,
        'api_st_lose': admiral.sortie_total - admiral.sortie_successes,
        'api_ms_count': admiral.expedition_total,
        'api_ms_success': admiral.expedition_successes,
        'api_pt_win': admiral.pvp_successes,
        'api_pt_lose': admiral.pvp_total - admiral.pvp_successes,
        'api_pt_challenged': 0,
        'api_pt_challenged_win': 0,
        # Disables the opening stuff, and skips straight to the game.
        'api_firstflag': 1 if admiral.setup else 0,
        'api_tutorial_progress': 100,
        'api_pvp': [0, 0]
    }

def get_admiral_sorties():
    """
    Gets Admiral's unlocked Sorties
    :return: A list containing dicts of KanColle Sortie info for the Admiral
    """
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

def new_admiral():
        """
        Sets up an admiral.
        This is for both APIv1 and APIv2.
        :param first_ship_id: The ID of the very first ship.
        :param admiral: The admiral object to setup.
        :return: The setup admiral.
        """
        admiral = Admiral()
        # Give the admiral starting resources
        admiral.resources = Resource(500,500,500,500,1,1,3,0)
        # Give the admiral some docks.
        docks = [Dock() for _ in range(8)]
        admiral.docks = docks
        # Return the admiral
        admiral.setup = False
        return admiral

def get_admiral_from_token(api_token=None):
    """
    Grabs an admiral object from the specified API token, or creates a new one if possible.
    :param api_token: Optional: The API token to use. If this is not specified, it uses the token from the POST request.
    :return: A valid admiral object.
    """ 

    # Get the API token.
    #if api_token is None:
    #   api_token = request.values.get('api_token', None)
    #if ALLOW_NO_API:
        #api_token = User().byId(id=1).api_token
    if api_token is None:
        return None

    # TODO: Optimize out some querying here
    user = User.query.filter_by(api_token=api_token).first()
    if not user:
        return None
    # Create a new admiral object if it doesn't exist.
    if not user.admiral:
        adm = new_admiral()
        user.admiral = adm
        db.session.add(user)
        db.session.commit()

    # Do resource creating here, rather than elsewhere.
    last = user.admiral.lastaction
    if last is None:
        last = datetime.datetime.utcnow()
    now = datetime.datetime.utcnow()

    # convert to unix timestamp
    d1_ts = time.mktime(now.timetuple())
    d2_ts = time.mktime(last.timetuple())

    minutes = math.floor(int(d1_ts-d2_ts) / 60)
    
    resources = ResourceHelper.get_resource_list(user.admiral.resources)    
    if minutes != 0:
        for n, val in enumerate(resources):
            if n >= 4:
                break
            resources[n] += (3 * minutes) if n != 3 else minutes
        user.admiral.resources = pack_resources(resources)
        user.admiral.lastaction = datetime.datetime.utcnow()

        db.session.add(user)
        db.session.commit()

    return user.admiral

def get_admiral_v2(api_token: str):
    """
    Grabs an admiral object from the specified API token, or creates a new one if possible, for APIv2.
    :param api_token: The API token to use. Not optional.
    :return: A valid admiral object, or None if the token is not valid.
    """
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
    """
    Grabs an admiral object from the specified API token or ID, or creates a new one if possible, for APIv2.
    :param search: The id or token to search.
    :return: A valid admiral object, or None if the token/id is not valid.
    """
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

def activate_quest(quest_id,admiral=None,admiral_id=None):
    admiral = admiral if admiral else Admiral.query.get(admiral_id)
    AdmiralQuest.query.filter_by(admiral_id=admiral.id,quest_id=quest_id).update({"state":2})
    db.session.commit()

def deactivate_quest(quest_id,admiral=None,admiral_id=None):
    admiral = admiral if admiral else Admiral.query.get(admiral_id)
    AdmiralQuest.query.filter_by(admiral_id=admiral.id,quest_id=quest_id).update({"state":1})
    db.session.commit()

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
    print('aaaa')
    resources = ResourceHelper.get_resource_list(admiral.resources)
    data = [{
        "api_id": n + 1,
        "api_member_id": admiral.id,
        "api_value": resource
    } for n,resource in enumerate(resources)]
    # I have no idea what this is, it can have any api_value
    # but without it flame/bucket/mat always show up as 0.
    data.append({"api_id": 8,"api_member_id": admiral.id,"api_value":1})
    print(data)
    return data


def admiral_grant_resources(admiral,resource=None,**kwargs):
    admiral.resources = ResourceHelper.update_resource(admiral.resources,resource,kwargs)
    db.session.add(admiral)
    db.session.commit()

def admiral_grant_item(admiral,item_id,quantity=1):
    for _ in range(quantity):
        db.session.add(AdmiralItem(admiral_id=admiral.id,item_id=item_id))
    db.session.commit()

def admiral_grant_ship(admiral,ship_id,quantity=1):
    pass
    #for _ in range(quantity):
        #db.session.add(AdmiralShip(admiral_id=admiral.id,item_id=item_id))
    #db.session.commit()
