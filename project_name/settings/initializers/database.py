from .base import env

DATABASES = {
    'default': env.db()
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
