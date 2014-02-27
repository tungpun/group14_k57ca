from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.board, name='board'),      # /timetables/pid=2
    url(r'^id=(?P<pid>\d+)', views.board, name='board'),      # /timetables/pid=2
    url(r'^add/$', views.add, name='add'),        # /timetables/add            ...add time table
)