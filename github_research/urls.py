from django.conf.urls import patterns, include, url
from django.contrib import admin

import main

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'github_research.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^/', include(main.urls)),
)
