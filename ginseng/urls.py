"""ginseng URL Configuration

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
		url(r'^sensordata/$', views.SensorData.as_view()),
		url(r'^sensor1_data/$', views.sensor1_data, name='sensor1_data'),
		url(r'^sensor2_data/$', views.sensor2_data, name='sensor2_data'),
		url(r'^sensor3_data/$', views.sensor3_data, name='sensor3_data'),
		url(r'^sensor4_data/$', views.sensor4_data, name='sensor4_data'),
		url(r'^check_status/$', views.check_status, name='check_status'),
		url(r'update_sensor/$', views.update_sensor, name='update_sensor'),
		url(r'get_selector/$', views.get_selector, name='get_selector'),
		)
