# Python imports

# project imports
from .initializers.base import *
from .initializers.apps import CUSTOM_APPS

# uncomment the following line to include others settings
# from .initializers.i18n import * # I18N Support
# from .initializers.auth import * # Authentication Support


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# adjust the minimal login
LOGIN_URL = 'core_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'core_login'

CUSTOM_APPS += (
    "debug_toolbar",
)

# Additional middleware introduced by debug toolbar
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': env.db()
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
