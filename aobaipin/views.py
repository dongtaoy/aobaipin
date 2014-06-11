# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    #return HttpResponse(html)
    return render(request, 'base.html', {"username": "你好"})

def world(request):
    return HttpResponse("World")