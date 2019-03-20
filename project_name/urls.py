"""{{ project_name }} URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

# Django imports
from django.conf import settings
from django.conf.urls import include, url, re_path
from django.conf.urls.static import static

from project_name.settings.initializers import admin
from .core import urls as core_urls

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^/?', include(core_urls, namespace='core')),

    # enable the admin interface
    url(r'^admin/', admin.site.urls),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [re_path("__debug__/", include(debug_toolbar.urls))]
