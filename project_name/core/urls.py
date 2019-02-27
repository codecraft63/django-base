from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views


app_name = 'core'
urlpatterns = [
    url(r'^$', views.home, name='home'),

    # provide the most basic login/logout functionality
    url(r'^login/$', auth_views.LoginView.as_view(), name='core_login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='core_logout'),

    # enable the admin interface
    url(r'^admin/', admin.site.urls),
]
