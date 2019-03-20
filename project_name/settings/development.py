# Python imports

# project imports
from .initializers.base import *

# uncomment the following line to include others settings
# from .initializers.i18n import * # I18N Support
# from .initializers.rest_framework import * # Django Rest Framework Support
# from .initializers.thumbnails import * # Django thumbnails utils
from .initializers.debug import * # Debug Toolbar Support
from .initializers.webpack import * # Webpack + VueJS Support


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
