from django.utils.translation import gettext_lazy as _

# uncomment the following line to enable others abilities
# from .extras.auth import * # Django Auth
# from .extras.admin import * # Django Admin (requires auth)
# from .extras.rest_framework import * # Django Rest Framework Support
# from .extras.thumbnails import * # Django thumbnails utils
# from .extras.dynamic_preferences import *  # Dynamic Preferences
# from .extras.celery import app as celery_app

# these persons receive error notification
ADMINS = (
    ('your name', 'your_name@example.com'),
)
MANAGERS = ADMINS

# Internationalization
USE_I18N = True

# This list of languages will be provided
LANGUAGES = (
    ('en-us', _('English')),
    ('pt-br', _('Brazilian Portuguese'))
)

# adjust the minimal login
LOGIN_URL = 'core_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'core_login'

LOCAL_APPS = [
    'app.core.apps.DefaultConfig'
]
