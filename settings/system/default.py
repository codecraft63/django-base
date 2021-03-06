# Python imports
import sys
from os.path import basename, dirname, exists

import environ

# ##### PATH CONFIGURATION ################################
ROOT_DIR = environ.Path(__file__) - 3

# load environment variables
env = environ.Env()

# Create a .env file in the project root directory
# But ideally this env file should be outside the git repo
# OS environment variables take precedence over variables from .env
env_file = ROOT_DIR('.env')
if exists(env_file):
    environ.Env.read_env(env_file)

# fetch Django's project directory
DJANGO_ROOT = ROOT_DIR.root

# fetch the project_root
PROJECT_ROOT = dirname(DJANGO_ROOT)

# the name of the whole site
SITE_NAME = env("SITE_NAME", default=basename(DJANGO_ROOT))
SITE_ID = 1

# social apps IDs
GTM_ID = env('GTM_ID', default='')
FACEBOOK_ID = env('FACEBOOK_ID', default='')

# collect static files here
STATIC_ROOT = ROOT_DIR('run', 'static')

# collect media files here
MEDIA_ROOT = ROOT_DIR('run', 'media')

# look for static assets here
STATICFILES_DIRS = [
    ROOT_DIR('public', 'static')
]

# look for templates here
# This is an internal setting, used in the TEMPLATES directive
PROJECT_TEMPLATES = [
    ROOT_DIR('templates'),
]

# add vendors/ to the Python path
sys.path.append(ROOT_DIR('vendors'))

# ##### APPLICATION CONFIGURATION #########################

DJANGO_APPS = [
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = []

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
                'django.template.context_processors.request',
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

# ##### SECURITY CONFIGURATION ############################

SECRET_KEY = env("SECRET_KEY")

# validates passwords (very low security, but hey...)
# AUTH_PASSWORD_VALIDATORS = [
#    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
#    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
#    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
#    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
# ]

# how many days a password reset should work. I'd say even one day is too long
# PASSWORD_RESET_TIMEOUT_DAYS = 1


# ##### DEBUG CONFIGURATION ###############################
DEBUG = env.bool("DJANGO_DEBUG", False)


AUTH_ENABLED = False
ADMIN_ENABLED = False
