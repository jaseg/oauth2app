#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from ldapOAuthProvider.apps.account.views import login, logout, clients

urlpatterns = patterns('',
    url(r'^login/?$', login, name='login'),
    url(r'^logout/?$', logout, name='logout'),
    url(r'^clients/?$', clients, name='clients'),
)
