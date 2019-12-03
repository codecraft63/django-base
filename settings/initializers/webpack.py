from .base import ROOT_DIR, THIRD_PARTY_APPS, DEBUG

THIRD_PARTY_APPS.append('webpack_loader')

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': 'assets/',
        'STATS_FILE': ROOT_DIR('static', 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': [
            r'.+\.hot-update.js',
            r'.+\.map'
        ]
    }
}
