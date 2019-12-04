"""{{ project_name }} URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

# Django imports
from django.conf import settings
from django.conf.urls import include
from django.urls import path, re_path

from .core import urls as core_urls

urlpatterns = [
    path('', include(core_urls, namespace='core')),
]

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [re_path("__debug__/", include(debug_toolbar.urls))]
