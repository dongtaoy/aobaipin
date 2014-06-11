# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from models.models import AbpErpAdmin
from django.template import RequestContext, loader
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
            request.session["uname"] = user.uname
            request.session["name"] = user.real_name
            request.session["u_id"] = user.adminid
            return redirect("/dashboard")

        raise Exception("mismatched password")
    except Exception as ex:
        return HttpResponse(ex)
        return render(request, "login.html", {"login_fail": 1})


def logout(request):
    del request.session["uname"]
    del request.session["name"]
    del request.session["u_id"]
    return redirect("/login")


def check_pass(salt, password, encrypted):
    return encrypted == md5(salt + password).hexdigest()


def login_status(request):
    try:
        return request.session["u_id"]
    except Exception:
        return None


def custom_context(request):
    return {
        "username": request.session["name"]
    }


def dashboard(request):
    return render(request, "dashboard.html", custom_context(request))
    return HttpResponse("dashboard")