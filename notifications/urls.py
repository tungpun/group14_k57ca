"""URLs configuration here"""
from django.conf.urls import patterns, url

import views


URLPATTERNS = patterns('',
                       url(r'^$', views.send_notification, name='send_notification'))
