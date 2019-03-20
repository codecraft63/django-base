# Python imports

# project imports
from .initializers.base import *
from .initializers.database import *
from .initializers.admin import *
from .project_apps import LOCAL_APPS

# uncomment the following line to include others settings
# from .initializers.i18n import * # I18N Support
# from .initializers.rest_framework import * # Django Rest Framework Support
# from .initializers.thumbnails import * # Django thumbnails utils
from .initializers.webpack import * # Webpack + VueJS Support


# ##### DEBUG CONFIGURATION ###############################
DEBUG = False

# allow all hosts during development
ALLOWED_HOSTS = []

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ##### SECURITY CONFIGURATION ############################

# TODO: Make sure, that sensitive information uses https
# TODO: Evaluate the following settings, before uncommenting them
# redirects all requests to https
# SECURE_SSL_REDIRECT = True
# session cookies will only be set, if https is used
# SESSION_COOKIE_SECURE = True
# how long is a session cookie valid?
# SESSION_COOKIE_AGE = 1209600

# the email address, these error notifications to admins come from
# SERVER_EMAIL = 'root@localhost'
