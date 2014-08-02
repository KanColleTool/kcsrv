from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import UserMixin, RoleMixin
from sqlalchemy.orm import configure_mappers
from sqlalchemy_continuum import make_versioned
from sqlalchemy_continuum.plugins import FlaskPlugin



# Initialize SQLAlchemy-Continuum
make_versioned(plugins=[FlaskPlugin()])



db = SQLAlchemy()

role__user = db.Table('role__user',
	db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	description = db.Column(db.Text)
	
	def __unicode__(self):
		return self.name

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	active = db.Column(db.Boolean)
	email = db.Column(db.String(255), unique=True, nullable=False)
	password = db.Column(db.String(255), nullable=False)
	confirmed_at = db.Column(db.DateTime())
	
	roles = db.relationship('Role', secondary=role__user, backref=db.backref('users', lazy='dynamic'))
	admiral = db.relationship('Admiral', backref='user', uselist=False)
	
	def __unicode__(self):
		return self.email



class Admiral(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	nickname = db.Column(db.String(255))
	last_login = db.Column(db.DateTime)
	level = db.Column(db.Integer, default=1)
	rank = db.Column(db.Integer, default=8)
	experience = db.Column(db.Integer, default=0)
	tutorial_progress = db.Column(db.Integer, default=0)
	
	furniture = db.Column(db.String(100), default="1,38,77,110,151,168")
	furniture_coins = db.Column(db.Integer, default=0)
	
	max_ships = db.Column(db.Integer, default=100)
	max_equips = db.Column(db.Integer, default=497)
	max_furniture = db.Column(db.Integer, default=0)
	available_fleets = db.Column(db.Integer, default=1)
	available_cdocks = db.Column(db.Integer, default=2)
	available_rdocks = db.Column(db.Integer, default=2)
	
	sortie_successes = db.Column(db.Integer, default=0)
	sortie_total = db.Column(db.Integer, default=0)
	expedition_successes = db.Column(db.Integer, default=0)
	expedition_total = db.Column(db.Integer, default=0)
	pvp_successes = db.Column(db.Integer, default=0)
	pvp_total = db.Column(db.Integer, default=0)



# Needed by SQLAlchemy-Continuum
configure_mappers()
