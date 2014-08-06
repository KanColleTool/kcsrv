import os
import string
import random
import datetime, time
import json
from flask import request, abort
import db

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

def generate_api_token():
	return ''.join(random.choice(string.hexdigits) for _ in range(40)).lower()

def svdata(obj, code=1, message="成功"):
	res = {
		"api_result": code,
		"api_result_msg": message,
		"api_data": obj
	}
	return ("svdata=" + json.dumps(res, separators=(',', ':')), 200, { "Content-Type": "text/plain" })

def load_datadump(filename):
	with open(os.path.join(ROOT_DIR, 'data', filename)) as f:
		o = json.load(f)
		return o if not 'api_data' in o else o['api_data']

def prepare_api_blueprint(bp):
	@bp.errorhandler(403)
	def api_403(e):
		return svdata({}, 100, "Unauthorized")

def get_token_admiral_or_error(api_token=None):
	if api_token is None:
		api_token = request.values.get('api_token', None)
	if api_token is None:
		abort(403)
	
	# TODO: Optimize out some querying here
	user = db.User.query.filter_by(api_token=api_token).first()
	if not user:
		abort(403)
	
	if not user.admiral:
		user.admiral = db.Admiral()
		db.db.session.add(user)
		db.db.session.commit()
	
	return user.admiral

def millisecond_timestamp(ts=datetime.datetime.now()):
	# http://stackoverflow.com/a/8160307
	time.mktime(ts.timetuple())*1e3 + ts.microsecond/1e3
