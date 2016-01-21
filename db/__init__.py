from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
This guarantees that we have all db classes, but also means that we might import things we don't need.
But then again, if we don't do this, we must be very careful about circular references.
We also bypass from db.admiral import Admiral and simply use from db import Admiral.
Overall, importing everything sounds like a reasonable choice.
"""

from db.support import *
from db.auth import *
from db.quests import *
from db.items import *
from db.admiral import *
from db.ships import *
from db.expedition import *