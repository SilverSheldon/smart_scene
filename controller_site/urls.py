from django.urls import path

from controller_site.views import main, about

urlpatterns = [
    path('', main),  # Главная страница: http://127.0.0.1/
    path('about', about),  # О нас: http://127.0.0.1/about
]