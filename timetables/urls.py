from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^board$', views.board, name='board'),      # /timetables/board/pid=2
    url(r'^$', views.board, name='index'),      # /timetables/pid=2
    #url(r'^id=(?P<pid>\d+)', views.board, name='board'),      # /timetables/pid=2
    url(r'^add/$', views.add, name='add'),        # /timetables/add            ...add time table
)