"""HajatRava URL Configuration

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
from WebServices import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^aboutus/$', views.get_about_us),
    url(r'^advMsg/$', views.get_ad_message),
    url(r'^tasks/(?P<task_id>\d+)/done$', views.set_task_done),
    url(r'^projects/projects/$', views.get_projects),
    url(r'^projects/(?P<project_id>\d+)/(?P<user_id>\d+)$', views.add_user_to_project),
    url(r'^tasks/(?P<project_id>\d+)/project$', views.get_project_tasks),
]
