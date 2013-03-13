from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('frontend.views',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',         'home',          name='home'),
    url(r'^register/', 'register',      name='register'),

)
