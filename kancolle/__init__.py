__author__ = 'me'

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import UserMixin, RoleMixin

db = SQLAlchemy()


"""
Tentative implementation of models. 
Package orm should not be used by other packages, only internally.

Instead of, for instance, using

from helpers import AdmiralHelper
AdmiralHelper.get_admiral_basic_info()

we use

from kancolle.admiral import Admiral
Admiral.get_basic_info()

The best part of this is not that it looks pretty, but the class Admiral extends AdmiralMap that extends db.Model.
This means that we get direct access to Admiral properties and we're able to create class methods while leaving the ORMap alone.

The naming does seems a bit reduntant and it's annoying me, but I haven't figured out what I want to do about it.
"""
