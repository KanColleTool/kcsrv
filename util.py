import os
import datetime
import time
import json
import math
from flask import request, abort

from db import db
from kancolle import User,Admiral

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

def svdata(obj: object, code: int=1, message: str="成功", errormsg: str="Invalid API request.") -> tuple:
    """
    Converts a json-serializable object into the KanColle APIv1 format response.
    :param obj: The object to convert.
        If this is None, an error will be produced instead.
    :param code: The 'status code'. Values used by KanColle are 1 for success, 200/201 for error.
    :param message: The message to respond with. Typically 成功 which means success.
    :param errormsg: Optional, this the error that should be provided.
    :return: svdata= + the JSON data required.
    """
    if obj is None:
        res = {
            "api_result": 201,
            "api_result_msg": errormsg,
            "api_data": obj
        }
    else:
        res = {
            "api_result": code,
            "api_result_msg": message,
            "api_data": obj
        }
    # Yay arbitary formats.
    return "svdata=" + json.dumps(res, separators=(',', ':')), 200, {"Content-Type": "text/plain"}


def load_datadump(filename: str) -> dict:
    """
    Loads a datadump from the data/ directory. Used primarily for api_start2, but can be used for other purposes.
    :param filename: The dump to load.
    :return: A dict containing the values loaded from either 'api_data' or the normal JSON data.
    """
    if not os.path.exists("data/" + filename):
        return {}
    with open(os.path.join(ROOT_DIR, 'data', filename)) as f:
        o = json.load(f)
        return o if 'api_data' not in o else o['api_data']


def prepare_api_blueprint(bp):
    @bp.errorhandler(403)
    def api_403(e):
        return svdata(None, 100, errormsg="Not authorized")


def get_token_admiral_or_error(api_token: str=None):
    ALLOW_NO_API = False
    """
    Grabs an admiral object from the specified API token, or creates a new one if possible.
    :param api_token: Optional: The API token to use. If this is not specified, it uses the token from the POST request.
    :return: A valid admiral object.
    """ 

    # Get the API token.
    if api_token is None:
        api_token = request.values.get('api_token', None)
    if ALLOW_NO_API:
        api_token = User().byId(id=1).api_token
    if api_token is None:
        abort(403)

    # TODO: Optimize out some querying here
    user = User.query.filter_by(api_token=api_token).first()
    if not user:
        abort(403)
    # Create a new admiral object if it doesn't exist.
    if not user.admiral:
        adm = Admiral.create()
        user.admiral = adm
        db.session.add(user)
        db.session.commit()

    # Do resource creating here, rather than elsewhere.
    last = user.admiral.lastaction

    if last is None:
        last = datetime.datetime.utcnow()

    now = datetime.datetime.utcnow()

    # convert to unix timestamp
    d1_ts = time.mktime(now.timetuple())
    d2_ts = time.mktime(last.timetuple())


    minutes = math.floor(int(d1_ts-d2_ts) / 60)

    resources = extract_resources(user.admiral.resources)

    if minutes != 0:
        for n, val in enumerate(resources):
            if n >= 4:
                break
            resources[n] += (3 * minutes) if n != 3 else minutes

        user.admiral.resources = pack_resources(resources)
        user.admiral.lastaction = datetime.datetime.utcnow()

        db.db.session.add(user)
        db.db.session.commit()

    return user.admiral

def pack_resources(r: list) -> str:
    return ",".join([str(x) for x in r])

def extract_resources(r: str) -> list:
    return list(map(int, (x for x in r.split(','))))

def get_admiral_v2(api_token: str):
    """
    Grabs an admiral object from the specified API token, or creates a new one if possible, for APIv2.
    :param api_token: The API token to use. Not optional.
    :return: A valid admiral object, or None if the token is not valid.
    """
    user = User.query.filter_by(api_token=api_token).first()
    if not user:
        return None
    if not user.admiral:
        adm = db.Admiral()
        user.admiral = adm
        db.db.session.add(user)
        db.db.session.commit()
    return user.admiral

def get_admiral_v2_from_id_or_token(search: object):
    """
    Grabs an admiral object from the specified API token or ID, or creates a new one if possible, for APIv2.
    :param search: The id or token to search.
    :return: A valid admiral object, or None if the token/id is not valid.
    """
    if len(search) == 40:
        user = User.query.filter_by(api_token=search).first()
    elif search:
        user = User.query.filter_by(id=search).first()
    else:
        return None
    if not user:
        return None
    if not user.admiral:
        adm = db.Admiral()
        user.admiral = adm
        db.db.session.add(user)
        db.db.session.commit()
    return user.admiral

def millisecond_timestamp(ts: datetime.datetime=datetime.datetime.now()) -> int:
    """
    Converts a timestamp into a millisecond timestamp.
    :param ts: Optional: The timestamp to use. Defaults to the current timestamp.
    :return: The unix timestamp in UTC for the specified timestamp.
    """
    # http://stackoverflow.com/a/8160307
    return math.floor(time.mktime(ts.timetuple()) * 1e3 + ts.microsecond / 1e3)


def take_items(l, indices):
    """
    Gets all items specified by the indices.
    >>> getlist = [1, 5, 7]
    >>> toget = [0, 2]
    >>> take_items(getlist, toget) # Gets items at index 0 and index 2 from the list.
    [1, 7]
    :param l: The list to search from.
    :param indices: The indices to get from the list.
    :return: A new list with the specified items.
    """
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
