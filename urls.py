from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'registry.views.home', name='home'),
    # url(r'^registry/', include('registry.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', direct_to_template, {'template' : 'site_base.html'}, name='home'),
    url(r'^400/$', direct_to_template, {'template': '404.html'}, name='400'),
    url(r'^500/$', direct_to_template, {'template': '500.html'}, name='500'),

)
