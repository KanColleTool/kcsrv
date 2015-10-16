from . import UserMixin, RoleMixin, db
import string, random

role__user = db.Table('role__user',
                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                      db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                      )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean)

    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    confirmed_at = db.Column(db.DateTime())

    nickname = db.Column(db.String(255), unique=True, nullable=False)
    api_token = db.Column(db.String(40), default=lambda: User.generate_api_token(), unique=True)

    admiral = db.relationship("Admiral", backref='user', uselist=False)

    roles = db.relationship('Role', secondary=role__user, backref=db.backref('users', lazy='dynamic'))  # Fix roles

    def __str__(self):
        return self.email

    def generate_api_token():
        """
        Generate a random API token.
        :return: A 40 character hexadecimal string.
        """
        return ''.join(random.choice(string.hexdigits) for _ in range(40)).lower()



class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)

    def __str__(self):
        return self.name