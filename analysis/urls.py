from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aobaipin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^shop_comparison/', 'analysis.views.shop_comparison'),
    url(r'^shop/(\d{1,2})/', 'analysis.views.shop_analysis'),
    url(r'^shop/', 'analysis.views.shop_analysis'),
    url(r'^ajax_graph/', 'analysis.ajax.ajax_graph')
)
