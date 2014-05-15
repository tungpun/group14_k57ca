"""URLs configuration here"""
from django.conf.urls import patterns, url

import views

URLPATTERNS = patterns('',
                       url(r'^auth_logout$', views.auth_logout, name='auth_logout'),
                       url(r'^auth_login$', views.auth_login, name='auth_login'),
                       url(r'^auth_register$', views.auth_register, name='auth_register'),
                       url(r'^gateway/do=(?P<pid>\d+)', views.gateway, name='gateway'),)
