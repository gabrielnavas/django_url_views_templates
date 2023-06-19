from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse('home page')

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('contact')
