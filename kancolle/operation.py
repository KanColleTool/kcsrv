from . import db

class Sortie(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    is_boss = db.Column(db.Integer, default=0)
    level = db.Column(db.String(10))

class Quest(db.Model):
    """
    no: quest number
    frequency: Once,Daily,Weekly
    category: Compostition, Exercise, etc.
    bonus_flag: ?
    invalid_flag: ?
    get_material: "[val,val,val,val]"
    code: A1,B20, etc. Not required. Maybe easier to maintain?
    """
    id = db.Column(db.Integer,primary_key=True)

    no = db.Column(db.Integer)
    category = db.Column(db.Integer)
    frequency = db.Column(db.Integer) #Kancolle calls it 'type'
    title = db.Column(db.String(255))
    detail = db.Column(db.Text)
    bonus_flag = db.Column(db.Integer)
    invalid_flag = db.Column(db.Integer)
    get_material = db.Column(db.String(25))
    code = db.Column(db.String(3))