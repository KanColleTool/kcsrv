from sqlalchemy.orm import reconstructor

from constants import *
from db.ships import Kanmusu
from db.quests import Quest
from . import db, Resources, Usable, QuestRequirement


class Admiral(db.Model):
    """
    If you have PyCharm, Collapse All (Ctrl + Shift + NumPad -) is recommended here.

    You have been warned.
    """
    __tablename__ = 'admiral'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    level = db.Column(db.Integer, default=1)
    experience = db.Column(db.Integer, default=0)
    rank = db.Column(db.Integer, default=8)

    furniture_coins = db.Column(db.Integer, default=0)

    max_kanmusu = db.Column(db.Integer, default=5000)
    max_equipment = db.Column(db.Integer, default=10000)
    max_furniture = db.Column(db.Integer, default=10000)

    sortie_total = db.Column(db.Integer, default=0)
    sortie_successes = db.Column(db.Integer, default=0)
    expedition_total = db.Column(db.Integer, default=0)
    expedition_successes = db.Column(db.Integer, default=0)
    pvp_total = db.Column(db.Integer, default=0)
    pvp_successes = db.Column(db.Integer, default=0)

    tutorial_progress = db.Column(db.Integer, default=0)
    last_action = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)

    resources_id = db.Column(db.ForeignKey('resources.id'))
    user_id = db.Column(db.ForeignKey('user.id'))

    furniture = db.relationship('AdmiralFurniture', lazy='dynamic')
    usables = db.relationship('AdmiralUsables', lazy='dynamic')
    equipment = db.relationship('AdmiralEquipment', lazy='dynamic')

    kanmusu = db.relationship('Kanmusu', order_by='Kanmusu.number', backref='admiral')
    resources = db.relationship('Resources')
    fleets = db.relationship('Fleet', order_by='Fleet.number')
    quests = db.relationship('Quest', lazy='dynamic')

    docks_craft = db.relationship("Dock",
        primaryjoin="and_(Admiral.id==Dock.admiral_id, Dock.type_== {})".format(DOCK_TYPE_CRAFT),
        order_by='Dock.number')
    docks_repair = db.relationship("Dock",
        primaryjoin="and_(Admiral.id==Dock.admiral_id, Dock.type_== {})".format(DOCK_TYPE_REPAIR),
        order_by='Dock.number')

    def get_questlist_ordered(self, exclude_hidden=True):
        """
        Here we get the quest list ordered by category and then by no.
        This is important to make sure we always show Composition->Sortie->Exercise etc
        """
        query = db.session.query(AdmiralQuest, Quest).order_by(Quest.category, Quest.no).filter(
            AdmiralQuest.quest_id == Quest.id, AdmiralQuest.admiral_id == self.id)
        if exclude_hidden:
            query = query.filter(AdmiralQuest.state != QUEST_STATE_HIDDEN)

        return query.all()

    def unlock_quest(self, quest_id):
        db.session.add(AdmiralQuest(admiral=self, quest_id=quest_id))
        db.session.commit()

    def complete_quest(self, quest_id=None, admiral_quest=None):
        if not admiral_quest:
            query = self.quests.filter(quest_id=quest_id)
            admiral_quest = query.first_or_404()
            quest = admiral_quest.quest
        else:
            quest = admiral_quest.quest

        # TODO: Fix this
        # AdmiralHelper.admiral_grant_resources(admiral, quest.reward)

        api_response = {'api_material': quest.reward.to_list(),
                        "api_bounus_count": quest.bonuses.count(),
                        "api_bounus": []}
        for bonus in quest.bonuses.all():
            """
            TODO unlock Fleet, LSC, etc.
            Also, I still can't get the effect announcing bonus items. They are added to Admiral's inventory,
            but the bonus reward announcent doesn't show up.
            """
            api_bonus = {
                "api_type": bonus.kind, "api_count": bonus.quantity
            }
            if bonus.kind == QUEST_REWARD_SHIP:
                ship = bonus.ship
                api_bonus["api_item"] = {
                    "api_ship_id": ship.id, "api_name": ship.name, "api_getmes": ship.getmsg
                }
                self.add_kanmusu(ship, bonus.quantity)
            elif bonus.kind == QUEST_REWARD_ITEM:
                api_bonus["api_item"] = {
                    "api_id": bonus.item_id, "api_name": ""
                }
                # TODO: Fix this
                # AdmiralHelper.admiral_grant_item(admiral, bonus.item_id, bonus.quantity)
            api_response["api_bounus"].append(api_bonus)

        db.session.query(AdmiralQuest).filter(AdmiralQuest.id == admiral_quest.id).update(
            {"state": QUEST_STATE_HIDDEN, "progress": QUEST_PROGRESS_0})
        db.session.commit()

        """Unlocking new quests"""
        list_maybe_unlocked = db.session.query(QuestRequirement).filter(QuestRequirement.required_id == quest.id).all()
        for maybe_unlocked in list_maybe_unlocked:
            """maybe_unlocked -> requires quest just completed, so it may be unlocked"""
            id_quest_maybe = maybe_unlocked.quest_id
            quests_required = db.session.query(QuestRequirement).filter(QuestRequirement.quest_id == id_quest_maybe).all()
            """quests_required -> all quests required to unlock maybe_unlocked"""
            number_required = len(quests_required)
            if number_required == 1:
                """We just completed the one needed, so might as well save one query"""
                self.unlock_quest(id_quest_maybe)
                break
            ids_required = [quest.required_id for quest in quests_required]
            """
            This basically checks if all quests_required have the state QUEST_STATE_HIDDEN.
            If the quest is missing from the list or is not marked as hidden, then the quest can't be unlocked.
            """
            quest_count = db.session.query(AdmiralQuest).filter(AdmiralQuest.state == QUEST_STATE_HIDDEN,
                AdmiralQuest.quest_id.in_(ids_required)).count()
            if number_required == quest_count:
                self.unlock_quest(quest_id)

        return api_response

    def activate_quest(self, quest_id):
        self.quests.filter_by(quest_id=quest_id).update({"state": 2})
        db.session.commit()

    def deactivate_quest(self, quest_id):
        self.quests.filter_by(quest_id=quest_id).update({"state":1})
        db.session.commit()

    def create(self, user):
        """
        Create a new Admiral.
        """
        self.resources = Resources(fuel=500, ammo=500, steel=500, baux=500)
        self.docks_craft = [Dock(type_=DOCK_TYPE_CRAFT, number=n + 1, resources=Resources().none()) for n in range(3)]
        self.docks_repair = [Dock(type_=DOCK_TYPE_REPAIR, number=n + 1, resources=Resources().none()) for n in range(3)]
        self.fleets = [Fleet(number=1)]

        # hm...must do better than this.
        initial_usables = [AdmiralUsables(usable=Usable.by_name(NAME_BUCKET), quantity=3),
                           AdmiralUsables(usable=Usable.by_name(NAME_FLAME), quantity=4),
                           AdmiralUsables(usable=Usable.by_name(NAME_MATERIAL), quantity=5),
                           AdmiralUsables(usable=Usable.by_name(NAME_SCREW), quantity=1)]
        self.usables = initial_usables
        """
        last = user.admiral.lastaction
        if last is None:
            last = datetime.datetime.utcnow()
        now = datetime.datetime.utcnow()

        # convert to unix timestamp
        d1_ts = time.mktime(now.timetuple())
        d2_ts = time.mktime(last.timetuple())

        minutes = math.floor(int(d1_ts-d2_ts) / 60)

        resources = user.admiral.resources.to_list()
        if minutes != 0:
            for n, val in enumerate(resources):
                if n >= 4:
                    break
                resources[n] += (3 * minutes) if n != 3 else minutes
            user.admiral.resources = pack_resources(resources)
            user.admiral.lastaction = datetime.datetime.utcnow()
        """
        user.admiral = self
        db.session.add(user)
        db.session.commit()
        return self

    # Not sure if this one is worth it.
    def add_item(self, item_id, item_type, quantity=1):
        if item_type == ITEM_TYPE_USABLE:
            usable = self.usables.find(lambda g: g.usables_id == item_id)
            if usable:
                usable.quantity += quantity
            else:
                self.usables.append(AdmiralUsables(usables_id=item_id, quantity=quantity))
        elif item_type == ITEM_TYPE_FURNITURE:
            for _ in range(quantity):
                self.items.append(AdmiralFurniture(furniture_id=item_id))
        elif item_type == ITEM_TYPE_EQUIPMENT:
            for _ in range(quantity):
                self.items.append(AdmiralEquipment(equipment_id=item_id))

    def get_usable(self, name):
        for u in self.usables:
            if u.usable.name == name:
                return u

        usable = Usable.by_name(name)
        if usable:
            ausable = AdmiralUsables(usable=usable, quantity=0)
            self.usables.append(ausable)
            return ausable
        return None

    def add_kanmusu(self, ship_id=None, ship_api_id=None, fleet_number=None, position=None):
        kanmusu = Kanmusu().create(ship_id, ship_api_id)
        kanmusu.number = len(self.kanmusu) + 1
        if fleet_number:
            self.fleets[fleet_number - 1].kanmusu.append(kanmusu)
            kanmusu.fleet_position = position if position else 1
        self.kanmusu.append(kanmusu)
        db.session.add(self)
        db.session.commit()


class AdmiralEquipment(db.Model):
    __tablename__ = 'admiral_equipment'

    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer)
    locked = db.Column(db.Integer)
    admiral_id = db.Column(db.ForeignKey('admiral.id'))
    equipment_id = db.Column(db.ForeignKey('equipment.id'))

    admiral = db.relationship('Admiral')
    equipment = db.relationship('Equipment')


class AdmiralFurniture(db.Model):
    __tablename__ = 'admiral_furniture'

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean)
    admiral_id = db.Column(db.ForeignKey('admiral.id'), index=True)
    furniture_id = db.Column(db.ForeignKey('furniture.id'), index=True)

    admiral = db.relationship('Admiral')
    furniture = db.relationship('Furniture')


class AdmiralUsables(db.Model):
    __tablename__ = 'admiral_usables'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    admiral_id = db.Column(db.ForeignKey('admiral.id'), index=True)
    usable_id = db.Column(db.ForeignKey('usable.id'), index=True)

    usable = db.relationship('Usable')


class AdmiralQuest(db.Model):
    __tablename__ = 'admiral_quest'

    id = db.Column(db.Integer, primary_key=True)
    progress = db.Column(db.Integer)
    state = db.Column(db.Integer)
    data = db.Column(db.String(255))
    admiral_id = db.Column(db.ForeignKey('admiral.id'))
    quest_id = db.Column(db.ForeignKey('quest.id'))

    admiral = db.relationship('Admiral')
    quest = db.relationship('Quest')


class Dock(db.Model):
    __tablename__ = 'dock'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    type_ = db.Column(db.Integer)
    state = db.Column(db.Integer)
    complete = db.Column(db.BigInteger)
    admiral_id = db.Column(db.ForeignKey('admiral.id'))
    kanmusu_id = db.Column(db.ForeignKey('kanmusu.id'))
    resources_id = db.Column(db.ForeignKey('resources.id'), index=True)

    resources = db.relationship('Resources', uselist=False)
    kanmusu = db.relationship('Kanmusu')

    @reconstructor
    def default_resources(self):
        if self.resources is None:
            self.resources = Resources(fuel=0, ammo=0, steel=0, baux=0)


class Fleet(db.Model):
    __tablename__ = 'fleet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, default="Unnamed")
    number = db.Column(db.Integer)
    admiral_id = db.Column(db.ForeignKey('admiral.id'))

    admiral = db.relationship('Admiral')
    kanmusu = db.relationship('Kanmusu')
