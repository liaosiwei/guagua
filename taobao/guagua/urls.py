from django.conf.urls import patterns, url

urlpatterns = patterns('guagua.views',
    url(r'^base/$', 'base'), 
)