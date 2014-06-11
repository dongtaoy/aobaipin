from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aobaipin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'aobaipin.views.index'),
    url(r'^login/', 'aobaipin.views.login'),
    url(r'^logout/', 'aobaipin.views.logout'),
    url(r'^dashboard/', 'aobaipin.views.dashboard'),
    url(r'^lock/', 'aobaipin.views.lock'),
    url(r'^admin/', include(admin.site.urls)),
)
