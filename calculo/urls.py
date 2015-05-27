from django.conf.urls import patterns, url

from calculo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^matriz/$', views.matriz),
)
