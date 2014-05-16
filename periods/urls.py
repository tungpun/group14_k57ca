"""URLs configuration here"""
from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^edit/id=(?P<pid>\d+)', views.edit, name='edit'),
                       url(r'^add/id=(?P<pid>\d+)$', views.add, name='add'),
                       url(r'^id=(?P<pid>\d+)', views.detail, name='detail'),
                       url(r'^enroll/id=(?P<pid>\d+)$', views.enroll, name='enroll'),
                       url(r'^remove/id=(?P<pid>\d+)$', views.remove, name='remove'),)
