from flask.ext.script import Manager, prompt, prompt_pass, prompt_bool
from flask.ext.security.utils import encrypt_password
import datetime
from db import *

manager = Manager(usage="Manage users")

@manager.command
def create(nickname, email):
	'''Create a user'''
	print "Nickname: %s" % nickname
	print "Email: %s" % email
	
	while True:
		password = prompt_pass("Password")
		if password == prompt_pass("Again"):
			break
	
	roles = prompt("Roles (separated by space)").split(' ')
	
	if prompt_bool("Create this user?"):
		user = User(active=True,
			email=email,
			password=encrypt_password(password),
			confirmed_at=datetime.datetime.now(),
			nickname=nickname,
			roles=[Role.query.filter_by(name=role).first_or_404() for role in roles]
		)
		db.session.add(user)
		db.session.commit()
