from . import db

class Equipment(db.Model):
    __tablename__ = 'equipment'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('equipment_id_seq'::regclass)")
    sortno = db.Column(db.Integer)
    api_id = db.Column(db.Integer)
    name = db.Column(db.String)
    info = db.Column(db.String)
    rarity = db.Column(db.String)
    types = db.Column(db.String)
    resources_id = db.Column(db.ForeignKey('resources.id'), index=True)
    stats_id = db.Column(db.ForeignKey('stats.id'), index=True)

    dismantling = db.relationship('Resources')
    stats = db.relationship('Stats')


class Furniture(db.Model):
    __tablename__ = 'furniture'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('furniture_id_seq'::regclass)")
    title = db.Column(db.String)
    number = db.Column(db.Integer)
    description = db.Column(db.Text)
    type_ = db.Column(db.Integer)
    rarity = db.Column(db.Text)
    season = db.Column(db.Integer)
    price = db.Column(db.Integer)
    sale_flag = db.Column(db.Boolean)


class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True, server_default="nextval('item_id_seq'::regclass)")
    api_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    description = db.Column(db.String)
    category = db.Column(db.Integer)
    type_ = db.Column(db.Integer)
    price = db.Column(db.Integer)