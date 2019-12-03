from .base import THIRD_PARTY_APPS, MIDDLEWARE

THIRD_PARTY_APPS += (
    "debug_toolbar",
)

# Additional middleware introduced by debug toolbar
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
