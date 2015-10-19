import os
import datetime
import time
import json
import math
import random
import string
from flask import request, abort

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
    from helpers.AdmiralHelper import get_admiral_from_token
    api_token = api_token if api_token is not None else request.values.get('api_token', None)
    admiral = get_admiral_from_token(api_token)
    return admiral if admiral else abort(403)

def pack_resources(r: list) -> str:
    return ",".join([str(x) for x in r])

def extract_resources(r: str) -> list:
    return list(map(int, (x for x in r.split(','))))


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

def generate_api_token():
        """
        Generate a random API token.
        :return: A 40 character hexadecimal string.
        """
        return ''.join(random.choice(string.hexdigits) for _ in range(40)).lower()