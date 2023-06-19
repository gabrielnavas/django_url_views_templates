from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('about page')

def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse('contact page')
