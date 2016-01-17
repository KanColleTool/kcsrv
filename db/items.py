from . import db


class Equipment(db.Model):
    __tablename__ = 'equipment'

    id = db.Column(db.Integer, primary_key=True)
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

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    number = db.Column(db.Integer)
    description = db.Column(db.Text)
    type_ = db.Column(db.Integer)
    rarity = db.Column(db.Text)
    season = db.Column(db.Integer)
    price = db.Column(db.Integer)
    sale_flag = db.Column(db.Boolean)


class Usable(db.Model):
    __tablename__ = 'usable'

    id = db.Column(db.Integer, primary_key=True)
    api_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    description = db.Column(db.String)
    description2 = db.Column(db.String) # Go figure.
    category = db.Column(db.Integer)
    type_ = db.Column(db.Integer)
    price = db.Column(db.Integer)


    def by_name(name):
        return db.session.query(Usable).filter(Usable.name == name).first()
