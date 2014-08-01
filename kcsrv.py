#!/usr/bin/env python
import os
from flask import Flask, render_template
from flask.ext.migrate import Migrate
from flask.ext.security import Security, SQLAlchemyUserDatastore
from db import *

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['DEBUG'] = None
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(ROOT_PATH, "kcsrv.db")
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.route('/')
def index():
	return render_template('index.html')
