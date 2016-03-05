from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'UI.views.homepage', name='home'),
    url(r'^main_options/$', 'UI.views.main_options', name='main_options'),
    url(r'^search_page/$', 'UI.views.search_page', name='search_page'),
    url(r'^upload_page/$', 'UI.views.upload_page', name='upload_page'),
    url(r'^request_page/$', 'UI.views.request_page', name='request_page'),
    url(r'^check_request_page/$', 'UI.views.check_request_status_page', name="check_request_status"),
    url(r'^query/', 'UI.views.query', name='query'),
    url(r'^lucky/', 'UI.views.lucky', name='lucky'),
    url(r'^view/(?P<identification>[A-Za-z0-9_\-]+)/$', 'UI.views.view', name='view'),
    url(r'^download/', 'UI.views.download', name='view'),
    url(r'^initials/(?P<full_name>(.*))/$', 'UI.views.initials', name='initials'),
    url(r'^cover/(?P<identification>[A-Za-z0-9_\-]+)/$', 'UI.views.cover', name='cover'),
]
