from django.conf.urls import patterns, url
from views import Login, Logout, Index, Register, Groups, Group, GroupCreate, GroupUpdate, GroupDelete

urlpatterns = patterns(
	'', 
	url(r'^$', Index.as_view(), name='index'),
	url(r'^login/$', Login.as_view(), name='login'),
	url(r'^logout/$', Logout.as_view(), name='logout'),
	url(r'^register/$', Register.as_view(), name='register'),
	url(r'^groups/$', Groups.as_view(), name='groups'),
    url(r'^group/add/$', GroupCreate.as_view(), name='group_create'),
    url(r'^group/(?P<pk>\d+)/$', GroupUpdate.as_view(), name='group_update'),
    url(r'^group/(?P<pk>\d+)/delete/$', GroupDelete.as_view(), name='group_delete'),
)