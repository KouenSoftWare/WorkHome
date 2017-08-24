#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url

from . import views

app_name = 'Home'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
]
