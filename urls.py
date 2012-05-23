from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', direct_to_template, {'template' : 'site_base.html'}, name='home'),
    url(r'^400/$', direct_to_template, {'template': '404.html'}, name='400'),
    url(r'^500/$', direct_to_template, {'template': '500.html'}, name='500'),
)
