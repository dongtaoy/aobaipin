from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello")

def world(request):
    return HttpResponse("World")