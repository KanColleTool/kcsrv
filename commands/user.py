import datetime

from flask.ext.script import Manager, prompt_pass, prompt_bool
from flask.ext.security.utils import encrypt_password

from db import db, User, Role


manager = Manager(usage="Manage users")


@manager.command
def create(nickname, email):
    '''Create a user'''
    print("Nickname: " + nickname)
    print("Email: " + email)

    while True:
        password = prompt_pass("Password")
        if password == prompt_pass("Again"):
            break

    roles = input("Roles (separated by space): ").split(' ')

    if prompt_bool("Create this user?"):
        user = User(active=True, email=email, password=encrypt_password(password), confirmed_at=datetime.datetime.now(),
            nickname=nickname, roles=[Role.query.filter_by(name=role).first_or_404() for role in roles if role != ''])
        db.session.add(user)
        db.session.commit()


@manager.command
def grant(nickname, role):
    '''Grant a role to a user'''
    user = User.query.filter_by(nickname=nickname).first_or_404()
    role = Role.query.filter_by(name=role).first_or_404()
    user.roles.append(role)
    db.session.add(user)
    db.session.commit()


@manager.command
def ungrant(nickname, role):
    '''Un-grant a role to a user'''
    user = User.query.filter_by(nickname=nickname).first_or_404()
    role = Role.query.filter_by(name=role).first_or_404()
    user.roles.remove(role)
    db.session.add(user)
    db.session.commit()
