from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    menu= [{"title":'home page'},{"title":'news page'},{"title":'home '}]
    return render(request,'index/index.html', {'title': "Home page", 'menu': menu})



def garilla(request):
    return HttpResponse("<h1>Garilla Page</h1>")

def ravshan(request ):
    return HttpResponse("<h1>Ravshan Page</h1>")

def ravshanInner(request, id ):
    return HttpResponse(f"<h1>Ravshan Page </h1> <br/>  parametr: {id}" )
def flew(request):
    return HttpResponse("<h1>Flew Page</h1>")


def pepsi(request):
    return HttpResponse("<h1>Pepsi Page</h1>")

def kola(request):
    return HttpResponse("<h1>Kola Page</h1>")