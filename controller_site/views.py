from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def main(request):
    return HttpResponse(content='<h1>Главная страница</h1>')


def about(request):
    return HttpResponse(content='<h2>Страница "О нас"</h2>')


def pageNotFound404(request, exception):
    return HttpResponseNotFound(content='<h1>Страница не найдена</h1>')

# def pageUnauthorized401(request, exception): pass
