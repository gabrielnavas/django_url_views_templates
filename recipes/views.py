from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    context = {
        'name': 'Gabriel'
    }
    return render(request, 'recipes/home.html', context, status=200)

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('about page')

def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse('contact page')
