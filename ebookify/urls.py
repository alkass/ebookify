"""ebookify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'UI.views.homepage', name='home'),
    url(r'^main_options/$', 'UI.views.main_options', name='main_options'),
    url(r'^search_page/$', 'UI.views.search_page', name='search_page'),
    url(r'^upload_page/$', 'UI.views.upload_page', name='upload_page'),
    url(r'^request_page/$', 'UI.views.request_page', name='request_page'),
    url(r'^query/', 'UI.views.query', name='query'),
    url(r'^lucky/', 'UI.views.lucky', name='lucky'),
    url(r'^view/(?P<identification>[A-Za-z0-9_\-]+)/$', 'UI.views.view', name='view'),
    url(r'^download/(?P<identification>[A-Za-z0-9_\-]+)/$', 'UI.views.download', name='view'),
    url(r'^initials/(?P<full_name>(.*))/$', 'UI.views.initials', name='initials'),
]
