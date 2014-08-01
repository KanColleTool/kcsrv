#!/usr/bin/env python
from flask import Flask, render_template
from flask.ext.migrate import Migrate
from flask.ext.security import Security, SQLAlchemyUserDatastore
from db import *
from admin import admin

app = Flask(__name__)
app.config['DEBUG'] = None
app.config.from_object('config_default')
app.config.from_object('config')

db.init_app(app)
admin.init_app(app)

migrate = Migrate(app, db)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/')
def index():
	return render_template('index.html')
