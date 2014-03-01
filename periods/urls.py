from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^edit/id=(?P<pid>\d+)', views.edit, name='edit'),
    url(r'^id=(?P<pid>\d+)', views.detail, name='detail'),
)