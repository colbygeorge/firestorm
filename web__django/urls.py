# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
#from django.contrib import admin
#from django.contrib.auth.views import logout, login
from django.contrib.staticfiles.views import serve
#admin.autodiscover()

from webpages._SiteWide.views import load_dutils_js
from webpages.kiosk.views import *


urlpatterns = [
    # These are Django canned pages
    #url(r'^accounts/logout/$', logout, {'next_page': '/'},
    #    name='logout'),
    #url(r'^accounts/login/$', login, {'template_name': 'admin/login.html'}),
    #url(r'^logout/$', logout, {'next_page': '/'}),
    #url(r'^admin/', include(admin.site.urls)),

    # This is the frowned-upon way of serving static files in Django
    url(r'^static/(?P<path>.*)$', serve, {'insecure': True}),

    # an awesome library for using named urls from within Javascript
    url(r'^js/dutils.conf.urls.js$', load_dutils_js,
        name='dutils_conf'),

    # These are custom to the Firestorm project
    url(r'^$', home, name='home'),

    url(r'^view/$', view_topics, name='view_topics'),

    url(r'^view/add$', create_topic, name='create_topic'),

    url(r'^view/edit(?P<topic_key>.*)/', update_topic,
        name='update_topic'),

    url(r'^view/delete(?P<topic_key>.*)/', remove_topic,
        name='remove_topic'),


    url(r'^schedule/$', schedule,
        name='schedule'),

    url(r'^reports/$', reports,
        name='reports'),
]
