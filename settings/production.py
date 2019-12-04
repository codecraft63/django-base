from .environment import *

# ##### DEBUG CONFIGURATION ###############################
DEBUG = False
DATABASE_DEBUG = False

# allow all hosts during development
ALLOWED_HOSTS = []

# ##### SECURITY CONFIGURATION ############################

# TODO: Make sure, that sensitive information uses https
# TODO: Evaluate the following settings, before uncommenting them
# redirects all requests to https
SECURE_SSL_REDIRECT = True
# session cookies will only be set, if https is used
SESSION_COOKIE_SECURE = True
# how long is a session cookie valid?
SESSION_COOKIE_AGE = 1209600

# the email address, these error notifications to admins come from
# SERVER_EMAIL = 'root@localhost'

from .application import *
