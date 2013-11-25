#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ldapOAuthProvider.apps.client.views',
    (r'^(?P<client_id>\w+)/?$',            'client'),
)
