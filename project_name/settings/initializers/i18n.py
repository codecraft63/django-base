# Python imports
from os.path import join

# Django imports
from django.utils.translation import ugettext_lazy as _

# project imports
from project_name.settings.initializers.common import PROJECT_ROOT, MIDDLEWARE

# ##### INTERNATIONALIZATION ##############################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Internationalization
USE_I18N = True

# Localisation
USE_L10N = True

# enable timezone awareness by default
USE_TZ = True

# This list of languages will be provided
LANGUAGES = (
    ('en-us', _('English')),
    ('pt-br', _('Brazilian Portuguese'))
)

# Look for translations in these locations
LOCALE_PATHS = (
    join(PROJECT_ROOT, 'locale'),
)

# Inject the localization middleware into the right position
_SESSION_MIDDLEWARE = 'django.contrib.sessions.middleware.SessionMiddleware'
MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('django.middleware.locale.LocaleMiddleware', x) if MIDDLEWARE[i-1] == _SESSION_MIDDLEWARE else (x, ))]
