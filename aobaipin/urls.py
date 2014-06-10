from django.conf.urls import patterns, include, url
import aobaipin
from aobaipin.views import world
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aobaipin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'aobaipin.views.hello'),
    url(r'^world/', world),
    url(r'^admin/', include(admin.site.urls)),
)
