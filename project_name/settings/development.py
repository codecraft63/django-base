# Python imports

# project imports
from .initializers.base import *
from .initializers.apps import LOCAL_APPS

# uncomment the following line to include others settings
# from .initializers.i18n import * # I18N Support
# from .initializers.auth import * # Authentication Support
# from .initializers.debug import * # Debug Toolbar Support


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': env.db()
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
