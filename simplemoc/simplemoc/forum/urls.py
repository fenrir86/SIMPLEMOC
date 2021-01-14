from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import ForumView
from . import views


urlpatterns = [
    url(r'^$', views.ForumView.as_view(), name='index'),
    path('thread/<slug>/', views.ThreadView.as_view()),
    url(r'^tag/(?P<tag>[\w_-]+)/$', views.ForumView.as_view(), name='index_tagged'),
    url(r'^respostas/(?P<pk>\d+)/correta/$', views.reply_correct,
        name='reply_correct'),
    url(r'^respostas/(?P<pk>\d+)/incorreta/$', views.reply_incorrect,
        name='reply_incorrect'),

    path('admin/', admin.site.urls),
]
