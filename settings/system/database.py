from .default import env

DATABASE_DEBUG=False
DATABASES = {
    'default': env.db()
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['TEST'] = { "NAME": "{}_test".format(DATABASES['default']['NAME']) }

# enable timezone awareness by default
USE_TZ = True
