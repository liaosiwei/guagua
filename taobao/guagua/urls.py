from django.conf.urls import patterns, url

urlpatterns = patterns('guagua.views',
    url(r'^base/$', 'base'),
    url(r'^$', 'index'),
    url(r'^plot/$', 'plot'),
    url(r'^plotdata/$', 'ajax_plotdata'),
    url(r'^pie/$', 'pie'),
    url(r'^piedata/$', 'ajax_piedata'),
)