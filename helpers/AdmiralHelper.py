import util
import db
from helpers import ShipHelper

def setup(first_ship_id: int, admiral: db.Admiral):
    """
    Sets up an admiral.
    This is for both APIv1 and APIv2.
    :param first_ship_id: The ID of the very first ship.
    :param admiral: The admiral object to setup.
    :return: The setup admiral.
    """
    if admiral.setup: return
    # Create a new ship.
    ship = ShipHelper.generate_new_ship(first_ship_id, 0)
    # Assign ship the correct local ship number.
    ship.local_ship_num = len(admiral.admiral_ships.all())
    # Create a new fleet.
    fleet = db.Fleet()
    # Add the ship to the first fleet.
    fleet.ships.append(ship)
    # Add the ship to the admiral
    admiral.admiral_ships.append(ship)
    # Add the fleet to the admiral
    admiral.fleets.append(fleet)
    # Give the admiral starting resources
    admiral.resources = "500,500,500,500,1,1,3,0"
    # Give the admiral some docks.
    docks = [db.Dock() for _ in range(8)]
    admiral.docks = docks
    # Return the admiral
    admiral.setup = True
    return admiral

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

