from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aplicacion.views', name='home'),
      url(r'^calculo/', include('calculo.urls')),
      url(r'^admin/', include(admin.site.urls)),
)
