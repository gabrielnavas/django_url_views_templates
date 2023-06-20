from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    context = {
        'name': 'Gabriel'
    }
    return render(request, 'recipes/home.html', context, status=200)
