from django.conf.urls import patterns, url

urlpatterns = patterns('guagua.views',
    url(r'^base/$', 'base'),
    url(r'^$', 'index'),
    url(r'^plotdata/$', 'ajax_plotdata'),
    url(r'^plot/$', 'plot'), 
)