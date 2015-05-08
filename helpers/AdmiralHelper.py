import util
import db
from helpers import generate_ship

def get_admiral_basic_info():
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
        'api_count_kdock': 0, #admiral.available_cdocks,
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


def setup(first_ship_id: int, admiral: db.Admiral):
    if admiral.setup: return
    # Create a new ship.
    ship = generate_ship.generate_new_ship(first_ship_id, 0)
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
    # Return the admiral
    admiral.setup = True
    return admiral