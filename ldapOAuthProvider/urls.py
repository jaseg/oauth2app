from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ldapOAuthProvider.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('ldapOAuthProvider.apps.account.urls')),
    url(r'^client/', include('ldapOAuthProvider.apps.client.urls')),
    url(r'^oauth2/', include('ldapOAuthProvider.apps.oauth2.urls')),
)
