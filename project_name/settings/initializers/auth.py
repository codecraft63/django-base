from .base import DJANGO_APPS, MIDDLEWARE

DJANGO_APPS += ['django.contrib.auth',]

# adjust the minimal login
LOGIN_URL = 'core_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'core_login'

# Inject the authentication middleware into the right position
_BEFORE_MIDDLEWARE = 'django.contrib.messages.middleware.MessageMiddleware'
MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('django.contrib.auth.middleware.AuthenticationMiddleware', x) if MIDDLEWARE[i-1] == _BEFORE_MIDDLEWARE else (x, ))]

# validates passwords (very low security, but hey...)
# AUTH_PASSWORD_VALIDATORS = [
#    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
#    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
#    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
#    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
# ]

# how many days a password reset should work. I'd say even one day is too long
# PASSWORD_RESET_TIMEOUT_DAYS = 1
