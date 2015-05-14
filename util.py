import os
import string
import random
import datetime
import time
import json
import math

from flask import request, abort

import db

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def generate_api_token():
    return ''.join(random.choice(string.hexdigits) for _ in range(40)).lower()


def svdata(obj, code=1, message="成功") -> tuple:
    res = {
        "api_result": code,
        "api_result_msg": message,
        "api_data": obj
    }
    # Yay arbitary formats.
    return "svdata=" + json.dumps(res, separators=(',', ':')), 200, {"Content-Type": "text/plain"}


def load_datadump(filename) -> dict:
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
        adm = db.Admiral()
        user.admiral = adm
        db.db.session.add(user)
        db.db.session.commit()
    return user.admiral


def millisecond_timestamp(ts=datetime.datetime.now()):
    # http://stackoverflow.com/a/8160307
    return math.floor(time.mktime(ts.timetuple()) * 1e3 + ts.microsecond / 1e3)

def second_timestamp():
    return int(time.time())


def take_items(l, indices):
    return (l[idx] for idx in indices)

# http://stackoverflow.com/questions/3438756/some-built-in-to-pad-a-list-in-python

def pad(iterable, padding='.', length=7):
    """
    >>> iterable = [1,2,3]
    >>> list(pad(iterable))
    [1, 2, 3, '.', '.', '.', '.']
    """
    for count, i in enumerate(iterable):
        yield i
    while count < length - 1:
        count += 1
        yield padding

# http://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-in-a-single-expression
def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z