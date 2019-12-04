from ..system.default import DJANGO_APPS, MIDDLEWARE, TEMPLATES

AUTH_ENABLED = True

DJANGO_APPS += ['django.contrib.auth']

# Inject the auth middleware into the right position
_SESSION_MIDDLEWARE = 'django.middleware.csrf.CsrfViewMiddleware'
MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    (x, 'django.contrib.auth.middleware.AuthenticationMiddleware',) if MIDDLEWARE[i - 1] == _SESSION_MIDDLEWARE else (x,))]

TEMPLATES[0]['OPTIONS']['context_processors'] += ['django.contrib.auth.context_processors.auth',]
