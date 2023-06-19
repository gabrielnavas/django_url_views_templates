from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("""
        <!DOCTYPE>
        <html>
            <head>
                <title>My Home</title>
            </head>
            <body>
                hello world 2
            </body>
        </html>
    
    """)

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('about page')

def contact(request: HttpRequest) -> HttpResponse:
    return HttpResponse('contact page')
