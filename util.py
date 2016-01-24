import datetime
import functools
import json
import math
import os
import random
import string
import time
import warnings
import constants

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def svdata(obj: object, code: int = 1, message: str = "成功", errormsg: str = "Invalid API request.") -> tuple:
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
            "api_result": 201, "api_result_msg": errormsg, "api_data": obj
        }
    else:
        res = {
            "api_result": code, "api_result_msg": message, "api_data": obj
        }
    # Yay arbitary formats.
    return "svdata=" + json.dumps(res, separators=(',', ':')), 200, {"Content-Type": "application/json"}


def load_datadump(filename: str) -> dict:
    """
    Loads a datadump from the data/ directory. Used primarily for api_start2, but can be used for other purposes.
    :param filename: The dump to load.
    :return: A dict containing the values loaded from either 'api_data' or the normal JSON data.
    """
    if not os.path.exists("data/" + filename):
        return {}
    with open(os.path.join(ROOT_DIR, 'data', filename), encoding="UTF-8") as f:
        o = json.load(f)
        return o if 'api_data' not in o else o['api_data']


def prepare_api_blueprint(bp):
    @bp.errorhandler(403)
    def api_403(e):
        return svdata(None, 100, errormsg="Not authorized"), 403

    @bp.errorhandler(400)
    def api_400(e):
        return svdata({"en_api_error": "Invalid data recieved."}, 201,
                      errormsg="申し訳ありませんがブラウザを再起動し再ログインしてください。"), 400

    @bp.errorhandler(404)
    def api_404(e):
        return svdata(None, 100, errormsg="Could not find the appropriate data for the request"), 404


def pack_resources(r: list) -> str:
    return ",".join([str(x) for x in r])


def extract_resources(r: str) -> list:
    return list(map(int, (x for x in r.split(','))))


def millisecond_timestamp(ts: datetime.datetime = datetime.datetime.now()) -> int:
    """
    Converts a timestamp into a millisecond timestamp.
    :param ts: Optional: The timestamp to use. Defaults to the current timestamp.
    :return: The unix timestamp in UTC for the specified timestamp.
    """
    if isinstance(ts, int):
        ts = datetime.datetime.fromtimestamp(ts)
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


def get_exp_required(level, current_exp):
    """
    Gets the exp required for the next level.
    :param level: The level to attain.
    :param current_exp: Your current exp.
    """
    total = sum(constants.EXP_LEVEL[:level + 1])
    return total - current_exp


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


def deprecated(func):
    '''This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.'''

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.warn_explicit(
            "Call to deprecated function {}.".format(func.__name__),
            category=DeprecationWarning,
            filename=func.func_code.co_filename,
            lineno=func.func_code.co_firstlineno + 1
        )
        return func(*args, **kwargs)

    return new_func
