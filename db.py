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
	
	def __unicode__(self):
		return self.email



# Needed by SQLAlchemy-Continuum
configure_mappers()
