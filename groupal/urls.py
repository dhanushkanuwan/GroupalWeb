from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'groupal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^web/', include('web.urls', namespace="web")),
    url(r'^admin/', include(admin.site.urls)),
)
