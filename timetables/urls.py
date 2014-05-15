"""URLs configuration here"""
from django.conf.urls import patterns, url

import views

URLPATTERNS = patterns('',
                       url(r'^board$', views.board, name='board'),
                       url(r'^add/$', views.add, name='add'))
