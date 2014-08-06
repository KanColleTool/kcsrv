import os
import string
import random
import json

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
