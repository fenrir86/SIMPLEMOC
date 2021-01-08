# -*- coding: utf-8 -*-

from django.conf.urls import url, include


from django.contrib.auth import  views
from . import views as auth_views

urlpatterns = [
    url(r'^$', auth_views.dashboard, name='dashboard'),
    url(r'^entrar/$', views.LoginView.as_view(template_name = "accounts/login.html"),name='login'),
    url(r'^sair/$', views.LogoutView.as_view(template_name = "home.html"),name='logout',),
    url(r'^cadastre-se/$', auth_views.register, name='register'),
    url(r'^nova-senha/$', auth_views.password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^editar/$', auth_views.edit, name='edit'),
    url(r'^editar-senha/$', auth_views.edit_password, name='edit_password'),

]
