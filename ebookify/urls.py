from django.conf.urls import include, url
from django.contrib import admin
from UI.views import homepage, search, query, lucky, view, download, cover
import UI

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', homepage, name='home'),
    url(r'^search/$', search, name='search_page'),
    url(r'^query/', query, name='query'),
    url(r'^lucky/', lucky, name='lucky'),
    url(r'^view/(?P<identification>[A-Za-z0-9_\-]+)/$', view, name='view'),
    url(r'^download/', download, name='view'),
    url(r'^cover/(?P<identification>[A-Za-z0-9_\-]+)/$', cover, name='cover'),
]
