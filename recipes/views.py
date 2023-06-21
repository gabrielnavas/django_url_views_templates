from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    context = {
        'name': 'Gabriel'
    }
    return render(request, 'recipes/pages/home.html', context, status=200)

def recipe(request: HttpRequest, id) -> HttpResponse:
    context = {
        'name': 'Gabriel'
    }
    return render(request, 'recipes/pages/recipe-view.html', context, status=200)
