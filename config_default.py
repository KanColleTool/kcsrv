#
# Default configuration; please don't edit
# Everything in here is overridden by config.py
#

import os



# Default to connecting to a sqlite database called "kcsrv.db"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
	os.path.join(os.path.dirname(os.path.abspath(__file__)), "kcsrv.db")

# Require new users to confirm their email address
SECURITY_CONFIRMABLE = True
# Allow users to register
SECURITY_REGISTERABLE = True
# Allow users to recover lost passwords
SECURITY_RECOVERABLE = True

# Security URL configuration
SECURITY_URL_PREFIX = '/account'
SECURITY_LOGIN_URL = '/login'
SECURITY_LOGOUT_URL = '/logout'
SECURITY_REGISTER_URL = '/create'
SECURITY_RESET_URL = '/forgot'
