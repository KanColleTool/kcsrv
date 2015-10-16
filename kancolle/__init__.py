__author__ = 'me'

from flask.ext.security import UserMixin, RoleMixin
from db import db

from kancolle.auth import *
from kancolle.navalbase import *
from kancolle.admiral import *
