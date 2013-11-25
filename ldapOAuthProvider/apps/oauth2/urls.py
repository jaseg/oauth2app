#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^missing_redirect_uri/?$', 'ldapOAuthProvider.apps.oauth2.views.missing_redirect_uri'),
        url(r'^authorize/?$', 'ldapOAuthProvider.apps.oauth2.views.authorize'),
        url(r'^token/?$', 'oauth2app.token.handler'),
)
