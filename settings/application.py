# uncomment the following line to include others settings
# from .initializers.rest_framework import * # Django Rest Framework Support
# from .initializers.thumbnails import * # Django thumbnails utils
# from .initializers.dynamic_preferences import *  # Dynamic Preferences
# from .celery import app as celery_app

# Internationalization
USE_I18N = True

# adjust the minimal login
LOGIN_URL = 'core_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'core_login'

LOCAL_APPS = [
    'app.core.apps.CoreConfig'
]
