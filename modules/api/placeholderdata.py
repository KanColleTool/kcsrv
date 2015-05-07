from util import *

deck = {
    'api_flagship': '0',
    'api_id': 1,
    'api_member_id': 1,
    'api_mission': [0, 0, 0, 0],
    'api_name': 'Fleet One',
    'api_name_id': '',
    'api_ship': [1, -1, -1, -1, -1, -1]
}

inazuma_ship = {
    'api_backs': 4,
    'api_bull': 16,
    'api_cond': 49,
    'api_exp': [34717, 383, 85],
    'api_fuel': 9,
    'api_id': 1,
    'api_kaihi': [56, 89],
    'api_karyoku': [30, 49],
    'api_kyouka': [14, 31, 16, 18, 0],
    'api_leng': 1,
    'api_locked': 1,
    'api_locked_equip': 0,
    'api_lucky': [12, 59],
    'api_lv': 26,
    'api_maxhp': 30,
    'api_ndock_item': [0, 0],
    'api_ndock_time': 0,
    'api_nowhp': 30,
    'api_onslot': [0, 0, 0, 0, 0],
    'api_raisou': [64, 79],
    'api_sakuteki': [15, 39],
    'api_sally_area': 0,
    'api_ship_id': 237,
    'api_slot': [194, 195, 3, -1, -1],
    'api_slotnum': 3,
    'api_sortno': 337,
    'api_soukou': [31, 49],
    'api_srate': 2,
    'api_taiku': [40, 49],
    'api_taisen': [33, 59]
}

unsetslot = { 'api_data': {'api_slottype21': [294, 231, 293, 239, 287, 238], 'api_slottype41': -1, 'api_slottype18': -1,
                          'api_slottype10': [53], 'api_slottype5': [261, 244, 262], 'api_slottype20': -1,
                          'api_slottype27': -1, 'api_slottype40': -1, 'api_slottype26': -1, 'api_slottype14': -1,
                          'api_slottype1': [44, 278], 'api_slottype6': [303], 'api_slottype4': -1, 'api_slottype34': -1,
                          'api_slottype29': -1, 'api_slottype38': -1, 'api_slottype11': -1, 'api_slottype33': -1,
                          'api_slottype19': -1, 'api_slottype36': -1, 'api_slottype39': -1, 'api_slottype3': -1,
                          'api_slottype12': -1, 'api_slottype25': -1, 'api_slottype8': -1, 'api_slottype31': -1,
                          'api_slottype2': -1, 'api_slottype28': -1, 'api_slottype30': [265, 263, 264],
                          'api_slottype7': -1, 'api_slottype9': -1, 'api_slottype35': -1, 'api_slottype16': -1,
                          'api_slottype24': -1, 'api_slottype37': -1, 'api_slottype23': -1, 'api_slottype32': -1,
                          'api_slottype17': -1, 'api_slottype22': -1, 'api_slottype15': -1, 'api_slottype13': -1}}

api_ports = load_datadump('port.json')
