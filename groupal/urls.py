from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'', include('groupal.apps.web.urls', namespace="web")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('groupal.apps.api.urls', namespace='api')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
