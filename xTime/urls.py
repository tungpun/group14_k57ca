from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'xTime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^periods/', include('periods.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^', include('timetables.urls')),
)
