from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),

    # provide the most basic login/logout functionality
    path('login/', auth_views.LoginView.as_view(), name='core_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='core_logout'),

    # enable the admin interface
    path('admin/', admin.site.urls),
]
