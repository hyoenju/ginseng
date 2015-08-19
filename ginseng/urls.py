"ginseng URL Configuration

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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.home, name="home"),
		url(r'^administer/', views.administer, name='administer'),
		url(r'^login/$', views.login, name="login"),	
		url(r'^logout/$', views.logout, name="logout"),
		url(r'^login_data/$', views.login_data, name="login_data"),
#		url(r'^index/', views.index, name='index'),
#		url(r'^graph_data/', views.graph_data, name="graph_data"),	
#		url(r'^test_data/', views.test_data, name="test_data"),
		)
