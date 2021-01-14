"""simplemoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from .core import urls as urls_core
from .courses import urls as urls_courses
from .accounts import urls as urls_accounts
from .forum import urls as urls_forum

from django.conf import settings
from django.conf.urls.static import static
"""
Padrão
urlpatterns = [
  # path('admin/', admin.site.urls),
]
"""

urlpatterns = [
    url(r'^', include((urls_core, "core"),namespace='core')),
    url(r'^conta/', include((urls_accounts, "accounts"), namespace='accounts')),
    url(r'^cursos/', include((urls_courses, "courses"),namespace='courses')),
    url(r'^forum/', include((urls_forum, "forum"),namespace='forum')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
