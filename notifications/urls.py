"""URLs configuration here"""
from django.conf.urls import patterns, url

import views


urlpatterns = patterns('',
                       url(r'^$', views.send_notification, name='send_notification'))
