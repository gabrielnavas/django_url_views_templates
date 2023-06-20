from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    context = {
        'name': 'Gabriel'
    }
    return render(request, 'recipes/pages/home.html', context, status=200)
