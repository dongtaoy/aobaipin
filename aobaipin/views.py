# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from models.models import AbpErpAdmin
from hashlib import md5

def index(request):
    if not(login_status(request)):
        return redirect("/login")

    #return HttpResponse(html)
    return redirect("/dashboard")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html', {})
    try:
        user = AbpErpAdmin.objects.get(uname=request.POST["uname"])
        if check_pass(user.salt, request.POST["password"], user.pass_field):
            return HttpResponse(BASE_DIR)

        raise Exception("mismatched password")
    except Exception as ex:
        return render(request, "login.html", {"alert": "账户或密码错误"})


def check_pass(salt, password, encrypted):
    return encrypted == md5(salt + password).hexdigest()

def login_status(request):
    try:
        return request.session["id"]
    except:
        return None
