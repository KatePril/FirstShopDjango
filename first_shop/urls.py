"""
URL configuration for first_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.views import about_us, contacts, questions
from blog.views import blog, details
from blog.urls import urlpatterns as blog_urls
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', about_us, name="about_us"),
    path('', about_us, name="index"),
    path('contacts/', contacts, name="contacts"),
    path('questions/', questions, name="questions"),
    path('blog/', include(blog_urls)),
    path('members/', include('members.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)