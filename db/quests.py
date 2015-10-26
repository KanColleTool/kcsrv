from . import db


class Quest(db.Model):
    __tablename__ = 'quest'

    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Integer)
    category = db.Column(db.Integer)
    type_ = db.Column(db.Integer)
    title = db.Column(db.String(255))
    detail = db.Column(db.Text)
    bonus_flag = db.Column(db.Integer)
    invalid_flag = db.Column(db.Integer)
    code = db.Column(db.String(3))
    resources_id = db.Column(db.ForeignKey('resources.id'))

    resources = db.relationship('Resources')


class QuestBonus(db.Model):
    __tablename__ = 'quest_bonus'

    id = db.Column(db.Integer, primary_key=True)
    type_ = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    quest_id = db.Column(db.ForeignKey('quest.id'))
    item_id = db.Column(db.ForeignKey('equipment.id'))
    ship_id = db.Column(db.ForeignKey('ship.id'))

    item = db.relationship('Equipment')
    quest = db.relationship('Quest')
    ship = db.relationship('Ship')


class QuestRequirement(db.Model):
    __tablename__ = 'quest_requirement'

    id = db.Column(db.Integer, primary_key=True)
    quest_id = db.Column(db.ForeignKey('quest.id'))
    required_quest_id = db.Column(db.ForeignKey('quest.id'))

    quest = db.relationship('Quest', primaryjoin='QuestRequirement.quest_id == Quest.id')
    required_quest = db.relationship('Quest', primaryjoin='QuestRequirement.required_quest_id == Quest.id')
