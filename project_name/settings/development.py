# Python imports

# project imports
from .initializers.base import *
from .initializers.database import *
from .initializers.apps import LOCAL_APPS

# uncomment the following line to include others settings
# from .initializers.i18n import * # I18N Support
from .initializers.auth import * # Authentication Support
# from .initializers.rest_framework import * # Django Rest Framework Support
from .initializers.debug import * # Debug Toolbar Support
from .initializers.webpack import * # Webpack + VueJS Support


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
