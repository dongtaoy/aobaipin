from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    #return HttpResponse(html)
    return render(request, 'base.html', {1:1})

def world(request):
    return HttpResponse("World")