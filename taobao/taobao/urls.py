from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^auth/$', 'guagua.views.fetchuserinfo'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    url(r'^pwd_change/$', 'django.contrib.auth.views.password_change', {'template_name': 'pwd_change.html', 'post_change_redirect': '/',
                                                                        'password_change_form': SetPasswordForm}),
    url(r'^', include('guagua.urls')),
    # Examples:
    # url(r'^$', 'taobao.views.home', name='home'),
    # url(r'^taobao/', include('taobao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
