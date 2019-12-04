from .system import *
from .application import *

# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ##### DJANGO RUNNING CONFIGURATION ######################

# the default WSGI application
WSGI_APPLICATION = 'settings.wsgi.application'

# the root URL configuration
ROOT_URLCONF = 'app.urls'

# the URL for static files
STATIC_URL = '/static/'

# the URL for media files
MEDIA_URL = '/media/'
