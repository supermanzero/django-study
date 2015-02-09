from django.conf.urls import patterns, include, url
from django.contrib import admin
from view import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djgtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^[A-Z]{1,3}/$', current_datetime),
    url(r'^$', search),
)
