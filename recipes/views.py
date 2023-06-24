from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from recipes.models import Recipe

from utils.recipes.factory import make_recipe

def home(request: HttpRequest) -> HttpResponse:
    recipes = Recipe.objects.all().order_by('-id')
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context, status=200)

def recipe(request: HttpRequest, id) -> HttpResponse:
    context = {
        'recipe': make_recipe(),
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe-view.html', context, status=200)
