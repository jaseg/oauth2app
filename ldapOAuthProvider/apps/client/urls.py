#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^(?P<client_id>\w+)/?$', 'ldapOAuthProvider.apps.client.views.client'),
)
