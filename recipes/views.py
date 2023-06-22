from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from utils.recipes.factory import make_recipe

def home(request: HttpRequest) -> HttpResponse:
    max_recipes_fake = 11
    context = {
        'recipes': [make_recipe() for _ in range(max_recipes_fake)],
    }
    return render(request, 'recipes/pages/home.html', context, status=200)

def recipe(request: HttpRequest, id) -> HttpResponse:
    context = {
        'recipe': make_recipe(),
    }
    return render(request, 'recipes/pages/recipe-view.html', context, status=200)
