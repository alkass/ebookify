from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'UI.views.homepage', name='home'),
    url(r'^search/$', 'UI.views.search_page', name='search_page'),
    url(r'^query/', 'UI.views.query', name='query'),
    url(r'^lucky/', 'UI.views.lucky', name='lucky'),
    url(r'^view/(?P<identification>[A-Za-z0-9_\-]+)/$', 'UI.views.view', name='view'),
    url(r'^download/', 'UI.views.download', name='view'),
    url(r'^cover/(?P<identification>[A-Za-z0-9_\-]+)/$', 'UI.views.cover', name='cover'),
]
