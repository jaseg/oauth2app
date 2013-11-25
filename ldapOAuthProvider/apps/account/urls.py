#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('ldapOAuthProvider.apps.account.views',
    (r'^login/?$',                  'login'),
    (r'^logout/?$',                 'logout'),
    (r'^clients/?$',                'clients'),
)
