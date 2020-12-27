# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contact, name='contact')

]