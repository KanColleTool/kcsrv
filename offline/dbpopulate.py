import util
from db import db, Equipment, Ship, Stats, Resources, Remodel, Usable

# from helpers import ResourceHelper
data = util.load_datadump('api_start2.json')

def items():
    items = data["api_mst_useitem"]
    count = 0
    for item in items:
        old = db.session.query(Usable).filter(Usable.api_id == item["api_id"]).first()
        # TODO - Update data if api_id already exists
        if old:
            continue
        i = Usable(
            api_id=item["api_id"],
            type_=item["api_usetype"],
            category=item["api_category"],
            name=item["api_name"],
            description=item["api_description"][0],
            description2=item["api_description"][1],
            price=item["api_price"]
        )
        db.session.add(i)
        print("Merged usables {} - {}".format(i.api_id, i.name))
        count += 1
    print("Updated Usable database, {} entries added.".format(count))
    db.session.commit()

def equip():
    equips = data["api_mst_slotitem"]
    count = 0
    for equip in equips:
        old = db.session.query(Equipment).filter(Equipment.api_id == equip["api_id"]).first()
        # TODO - Update data if api_id already exists
        if old:
            continue
        e = Equipment(
            sortno=equip["api_sortno"],
            api_id=equip["api_id"],
            info=equip["api_info"],
            name=equip["api_name"],
            rarity=equip["api_rare"],
            types=equip["api_type"],
            stats=Stats(
                hp=equip["api_taik"],
                armour=equip["api_souk"],
                firepower=equip["api_houg"],
                torpedo=equip["api_raig"],
                speed=equip["api_soku"],
                dive_bomber=equip["api_baku"],
                antiair=equip["api_tyku"],
                antisub=equip["api_tais"],
                accuracy=equip["api_houm"],
                evasion=equip["api_houk"],
                los=equip["api_saku"],
                luck=equip["api_luck"],
                range_=equip["api_leng"],
            ),
            dismantling=Resources(
                fuel=equip["api_broken"][0],
                ammo=equip["api_broken"][1],
                steel=equip["api_broken"][2],
                baux=equip["api_broken"][3],
            )
        )
        """
        Ignored fields:
        usebull = equip["api_usebull"],
        raim = equip["api_raim"],
        atap = equip["api_atap"],
        raik = equip["api_raik"],
        bakk = equip["api_bakk"],
        sakb = equip["api_sakb"],
        """
        db.session.add(e)
        print("Merged equip {} - {}".format(e.api_id, e.name))
        count += 1
    print("Updated Equipment database, {} entries added.".format(count))
    db.session.commit()

def ships():
    ships = data['api_mst_ship']
    count = 0
    for ship in ships:
        if 'api_backs' not in ship:
            print("Skipping ship ID {}".format(ship['api_id']))
            continue
        old = db.session.query(Ship).filter(Ship.api_id == ship["api_id"]).first()
        # TODO - Update data if api_id already exists
        if old:
            continue
        s = Ship(
            # Misc ship stats
            api_id=ship['api_id'],
            rarity=ship['api_backs'],
            name=ship['api_name'],
            number=ship['api_sortno'],
            type_=ship['api_stype'],
            voicef=ship['api_voicef'],
            getmsg=ship['api_getmes'],
            buildtime=ship['api_buildtime'],
            kai='改' in ship['api_name'],
            dismantling=Resources(
                fuel=ship["api_broken"][0],
                ammo=ship["api_broken"][1],
                steel=ship["api_broken"][2],
                baux=ship["api_broken"][3],
            ),
            modernization=Resources(
                fuel=ship['api_powup'][0],
                ammo=ship['api_powup'][1],
                steel=ship['api_powup'][2],
                baux=ship['api_powup'][3],
            ),
            # Remodel
            remodel=Remodel(
                level=ship['api_afterlv'],
                remodel_api_id=ship['api_aftershipid'],
                cost=Resources(
                    fuel=ship['api_afterfuel'],
                    ammo=ship['api_afterbull']
                )
            ),
            # Minimums
            base_stats=Stats(
                luck=ship['api_luck'][0],
                firepower=ship['api_houg'][0],
                armour=ship['api_souk'][0],
                torpedo=ship['api_raig'][0],
                antiair=ship['api_tyku'][0],
                antisub=0,
                los=0,
                evasion=0,
                hp=ship['api_taik'][0],
            ),
            # Maximums
            max_stats=Stats(
                luck=ship['api_luck'][1],
                firepower=ship['api_houg'][1],
                armour=ship['api_souk'][1],
                torpedo=ship['api_raig'][1],
                antiair=ship['api_tyku'][1],
                antisub=0,
                los=0,
                evasion=0,
                range_=ship['api_leng'],
                hp=ship['api_taik'][1],
                ammo=ship['api_bull_max'],
                fuel=ship['api_fuel_max'],

            ),
            maxslots=ship['api_slot_num'],
            maxplanes=','.join(str(x) for x in ship['api_maxeq'])
        )
        # ugh
        db.session.add(s)
        print("Added ship {} - {}".format(ship['api_id'], ship['api_name']))
        count += 1
    db.session.commit()
    print("Updated Ship database, {} entries merged.".format(count))

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
            voicef = ship['api_voicef'],
            getmsg = ship['api_getmes'],
            buildtime = ship['api_buildtime'],
            kai = '改' in ship['api_name'],
            # Remodel
            remodel_level = ship['api_afterlv'],
            remodel = ship['api_aftershipid'],
            remodel_cost = Resource(fuel=ship['api_afterfuel'],ammo=ship['api_afterbull']),
            modernization = Stats(
                firepower=ship['api_powup'][0],
                torpedo=ship['api_powup'][1],
                antiair=ship['api_powup'][2],
                armour=ship['api_powup'][3],
            ),
            # Minimums
            stats = Stats(
                srange = ship['api_leng'],
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
            stats_max = Stats(
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
"""
