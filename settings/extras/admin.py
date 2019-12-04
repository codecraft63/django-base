from django.contrib import admin

from ..system.default import ADMIN_ENABLED, DJANGO_APPS

ADMIN_ENABLED = True

# Personalized admin site settings like title and header
admin.site.site_title = "{{ project_name|title }} Admin"
admin.site.site_header = "{{ project_name|title }} Administration"

DJANGO_APPS += [
    'django.contrib.admin',
]
