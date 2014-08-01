#!/usr/bin/env python
import os
from flask import Flask, render_template
from flask.ext.migrate import Migrate
from db import db

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(ROOT_PATH, "kcsrv.db")
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
	return render_template('index.html')
