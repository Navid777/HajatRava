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
    url(r'^projects/projects/(?P<username>\w*)$', views.get_projects),
    url(r'^projects/(?P<project_id>\d+)/(?P<username>\w+)$', views.add_user_to_project),
    url(r'^remove_user_from_project/(?P<project_id>\d+)/(?P<username>\w+)$', views.remove_member_from_project),
    url(r'^remove_project_for_all/(?P<project_id>\d+)/(?P<username>\w+)$', views.remove_project_for_all),
    url(r'^tasks/(?P<project_id>\d+)/project$', views.get_project_tasks),
    url(r'^user_tasks/(?P<username>\w+)$', views.get_user_tasks),
    url(r'^login/$', views.login),
    url(r'^create_user/$', views.create_user),
    url(r'^records/(?P<username>\w+)$', views.records),
    url(r'^get_project_info/(?P<username>\w+)/(?P<project_id>\d+)$', views.get_project_information),
    url(r'^get_project_info/(?P<project_id>\d+)$', views.get_project_information_without_user),
    url(r'^create_project_by_user/$', views.create_project_by_user),
]
