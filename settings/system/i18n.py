# Python imports
from os.path import join

# project imports
from .default import PROJECT_ROOT, MIDDLEWARE

# ##### INTERNATIONALIZATION ##############################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Internationalization
USE_I18N = True

# Localisation
USE_L10N = True

# Look for translations in these locations
LOCALE_PATHS = (
    join(PROJECT_ROOT, 'locale'),
)

# Inject the localization middleware into the right position
_SESSION_MIDDLEWARE = 'django.contrib.sessions.middleware.SessionMiddleware'
MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('django.middleware.locale.LocaleMiddleware', x) if MIDDLEWARE[i - 1] == _SESSION_MIDDLEWARE else (x,))]
