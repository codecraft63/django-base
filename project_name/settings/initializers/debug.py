from .base import LOCAL_APPS, MIDDLEWARE

LOCAL_APPS += (
    "debug_toolbar",
)

# Additional middleware introduced by debug toolbar
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
