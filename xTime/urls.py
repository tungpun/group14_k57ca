"""URLs configuration here"""
from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^periods/', include('periods.urls')),
                       url(r'^users/', include('users.urls')),
                       url(r'^notifications/', include('notifications.urls')),
                       url(r'^', include('timetables.urls')),
                       url(r'^favicon\.ico$', RedirectView.as_view(url='../static/image/favi3.ico')),)
