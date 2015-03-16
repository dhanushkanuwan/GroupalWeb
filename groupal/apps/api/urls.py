from django.conf.urls import patterns, url
from views import TestList

urlpatterns = patterns(
	'',
	url(r'^tests/$', TestList.as_view(), name='tests'),
    url(r'^tests/(?P<pk>[0-9]+)/$', TestList.as_view(), name='test'),
)
