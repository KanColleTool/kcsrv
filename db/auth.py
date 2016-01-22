from flask.ext.security import UserMixin, RoleMixin

from util import generate_api_token
from . import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    confirmed_at = db.Column(db.DateTime)
    nickname = db.Column(db.String(255), nullable=False, unique=True)

    api_token = db.Column(db.String(40), default=lambda: generate_api_token(), unique=True)

    roles = db.relationship('Role', secondary='role__user')

    admiral = db.relationship("Admiral", uselist=False)

    def __repr__(self):
        return "{} ({})".format(self.email, self.nickname)


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    description = db.Column(db.Text)

    users = db.relationship('User', secondary='role__user')


t_role__user = db.Table('role__user', db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')))
