# Python imports
from os.path import basename, dirname
import sys
import environ

# ##### PATH CONFIGURATION ################################
ROOT_DIR = environ.Path(__file__) - 4

# load environment variables
env = environ.Env()

# Create a .env file in the project root directory
# But ideally this env file should be outside the git repo
# OS environment variables take precedence over variables from .env
env_file = ROOT_DIR.path(".env")
if env_file.exists():
    environ.Env.read_env(str(env_file))


# fetch Django's project directory
DJANGO_ROOT = str(ROOT_DIR)

# fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

# the name of the whole site
SITE_NAME = env("SITE_NAME", basename(str(DJANGO_ROOT)))

# collect static files here
STATIC_ROOT = str(ROOT_DIR('run', 'static'))

# collect media files here
MEDIA_ROOT = str(ROOT_DIR('run', 'media'))

# look for static assets here
STATICFILES_DIRS = [
    str(ROOT_DIR('static')),
]

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    str(ROOT_DIR('templates')),
]

# add apps/ to the Python path
sys.path.append(str(ROOT_DIR('apps')))

# ##### APPLICATION CONFIGURATION #########################

# these are the apps
DJANGO_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

THIRD_PARTY_APPS = [
    'rest_framework',
]

LOCAL_APPS = []

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# template stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

# Internationalization
USE_I18N = False


# ##### SECURITY CONFIGURATION ############################

SECRET_KEY = env("SECRET_KEY")

# these persons receive error notification
ADMINS = (
    ('your name', 'your_name@example.com'),
)
MANAGERS = ADMINS


# ##### DJANGO RUNNING CONFIGURATION ######################

# the default WSGI application
WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

# the root URL configuration
ROOT_URLCONF = '%s.urls' % SITE_NAME

# the URL for static files
STATIC_URL = '/static/'

# the URL for media files
MEDIA_URL = '/media/'


# ##### DEBUG CONFIGURATION ###############################
DEBUG = env.bool("DJANGO_DEBUG", False)
