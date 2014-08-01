from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import UserMixin, RoleMixin

db = SQLAlchemy()

role__user = db.Table('role__user',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	description = db.Column(db.Text)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	active = db.Column(db.Boolean)
	email = db.Column(db.String(255), unique=True)
	username = db.Column(db.String(16), unique=True)
	password = db.Column(db.String(255), nullable=False)
	confirmed_at = db.Column(db.DateTime())
	
	roles = db.relationship('Role', secondary=role__user, backref=db.backref('users', lazy='dynamic'))
