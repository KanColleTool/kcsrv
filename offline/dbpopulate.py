import util
from db import db,Ship,Item,Resource,Stats
from helpers import ResourceHelper
data = util.load_datadump('api_start2.json')

def items():
    items = data["api_mst_slotitem"]
    count = 0
    for item in items:
        i = Item(
        sortno = item["api_sortno"],
        api_id = item["api_id"],
        name = item["api_name"],
        types = item["api_type"], #
        taik = item["api_taik"],
        souk = item["api_souk"],
        houg = item["api_houg"],
        raig = item["api_raig"],
        soku = item["api_soku"],
        baku = item["api_baku"],
        tyku = item["api_tyku"],
        tais = item["api_tais"],
        atap = item["api_atap"],
        houm = item["api_houm"],
        raim = item["api_raim"],
        houk = item["api_houk"],
        raik = item["api_raik"],
        bakk = item["api_bakk"],
        saku = item["api_saku"],
        sakb = item["api_sakb"],
        luck = item["api_luck"],
        leng = item["api_leng"],
        rarity = item["api_rare"],
        broken = item["api_broken"],
        info = item["api_info"],
        usebull = item["api_usebull"]
        )
        # mercy
        db.session.add(i)
    db.session.commit()
"""
def ships():
    ships = data['api_mst_ship']
    count = 0
    for ship in ships:
        if 'api_backs' not in ship:
            print("Skipping ship ID {}".format(ship['api_id']))
            continue
        s = Ship(
            # Misc ship stats
            rarity = ship['api_backs'],
            broken = ship['api_broken'],
            name = ship['api_name'],
            number = ship['api_sortno'],
            stype = ship['api_stype'],
            modern_use = ship['api_powup'],
            voicef = ship['api_voicef'],
            getmsg = ship['api_getmes'],
            srange = ship['api_leng'],
            buildtime = ship['api_buildtime'],
            kai = '改' in ship['api_name'],
            # Remodel
            afterlv = ship['api_afterlv'],
            aftership_num = ship['api_aftershipid'],
            remodel_cost = ','.join([str(ship['api_afterfuel']), str(ship['api_afterbull'])]),
            # Minimums
            luck_base = ship['api_luck'][0],
            firepower_base = ship['api_houg'][0],
            armour_base = ship['api_souk'][0],
            torpedo_base = ship['api_raig'][0],
            antiair_base = ship['api_tyku'][0],
            antisub_base = 0,
            los_base = 0,
            evasion_base = 0,
            hp_base = ship['api_taik'][0],
            # Maximums
            luck_max = ship['api_luck'][1],
            firepower_max = ship['api_houg'][1],
            armour_max = ship['api_souk'][1],
            torpedo_max = ship['api_raig'][1],
            antiair_max = ship['api_tyku'][1],
            antisub_max = 0,
            maxhp = ship['api_taik'][1],
            maxslots = ship['api_slot_num'],
            ammo_max = ship['api_bull_max'],
            fuel_max = ship['api_fuel_max'],
            maxlos = 0,
            evasion_max = 0,
            maxplanes = ','.join(str(x) for x in ship['api_maxeq'])
        )
        # ugh
        db.session.add(s)
        print("Added ship {} - {}".format(ship['api_id'], ship['api_name']))
        count += 1
    db.session.commit()
    print("Updated database, {} entries merged.".format(count))
"""

def ships():
    ships = data['api_mst_ship']
    count = 0
    for ship in ships:
        if 'api_backs' not in ship:
            print("Skipping ship ID {}".format(ship['api_id']))
            continue
        s = Ship(
            # Misc ship stats
            api_id = ship['api_id'],
            rarity = ship['api_backs'],
            broken = ResourceHelper.get_resource_from_list(ship['api_broken']),
            name = ship['api_name'],
            number = ship['api_sortno'],
            stype = ship['api_stype'],
            modern_use = ship['api_powup'],
            voicef = ship['api_voicef'],
            getmsg = ship['api_getmes'],
            srange = ship['api_leng'],
            buildtime = ship['api_buildtime'],
            kai = '改' in ship['api_name'],
            # Remodel
            remodel_level = ship['api_afterlv'],
            remodel = ship['api_aftershipid'],
            remodel_cost = Resource(fuel=ship['api_afterfuel'],ammo=ship['api_afterbull']),
            # Minimums
            stats = Stats(
                luck = ship['api_luck'][0],
                firepower = ship['api_houg'][0],
                armour = ship['api_souk'][0],
                torpedo = ship['api_raig'][0],
                antiair = ship['api_tyku'][0],
                antisub = 0,
                los = 0,
                evasion = 0,
                hp = ship['api_taik'][0],
            ),
            # Maximums
            max_stats = Stats(
                luck = ship['api_luck'][1],
                firepower = ship['api_houg'][1],
                armour = ship['api_souk'][1],
                torpedo = ship['api_raig'][1],
                antiair = ship['api_tyku'][1],
                antisub = 0,
                los = 0,
                evasion = 0,
                hp = ship['api_taik'][1],            
                ammo = ship['api_bull_max'],
                fuel = ship['api_fuel_max'],
            ),
            maxslots = ship['api_slot_num'],
            maxplanes = ','.join(str(x) for x in ship['api_maxeq'])
        )
        # ugh
        db.session.add(s)
        print("Added ship {} - {}".format(ship['api_id'], ship['api_name']))
        count += 1
    db.session.commit()
    print("Updated database, {} entries merged.".format(count))