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
    url(r'^view/(?P<identification>(([A-Za-z0-9]+[-])+[A-Za-z0-9]+)+)/$', 'UI.views.view', name='view'),
    url(r'^random/$', 'UI.views.view_random', name='random'),
    url(r'^download/(?P<identification>(([A-Za-z0-9]+[-])+[A-Za-z0-9]+)+)/$', 'UI.views.download', name='view'),
    url(r'^qr/(?P<identification>(([A-Za-z0-9]+[-])+[A-Za-z0-9]+)+)/$', 'UI.views.qr', name='qr'),
    url(r'^initials/(?P<full_name>(.*))/$', 'UI.views.initials', name='initials'),
]
