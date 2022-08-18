from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def ola(request):
    return render(request, 'cu.html')

def home(request):
    site = "<h1>oi</h1>"
    return HttpResponse(site)

def teste(request):
    site = 'cu'
    return HttpResponse(site)

   