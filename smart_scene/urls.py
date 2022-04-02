"""smart_scene URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from controller_site.views import pageNotFound404#, pageUnauthorized401

urlpatterns = [
    path('admin/', admin.site.urls), # Админка: http://127.0.0.1/admin/
    path('', include('controller_site.urls')),  # Главная страница: http://127.0.0.1/
]

handler404 = pageNotFound404
# handler401 = pageUnauthorized401