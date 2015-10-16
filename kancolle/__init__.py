__author__ = 'me'

from flask.ext.security import UserMixin, RoleMixin
from db import db
from kancolle.auth import *
from kancolle.classes import *
from kancolle.api import *