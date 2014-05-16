"""URLs configuration here"""
from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
                       url(r'^board$', views.board, name='board'),
                       url(r'^$', views.board, name='index'),
                       url(r'^add/$', views.add, name='add'))
