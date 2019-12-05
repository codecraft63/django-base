from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
]

if settings.ADMIN_ENABLED:
    from django.contrib import admin

    urlpatterns += [path('admin/', admin.site.urls)]

if settings.AUTH_ENABLED:
    from django.contrib.auth import views as auth_views

    urlpatterns += [
        # provide the most basic login/logout functionality
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]
