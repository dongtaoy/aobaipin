# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count
from models.models import AbpErpAdmin, AbpErpRetail, AbpItem, AbpUser
from django.template import RequestContext
from hashlib import md5
import time
import datetime


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
    ## sales, members, orders, products
    ## get sales
    dic = {}
    today = datetime.date.today()
    tommorrow = datetime.date.today() + datetime.timedelta(days=1)
    range = time_range(today, tommorrow)
    retail_data = AbpErpRetail.objects.filter(create_time__gte=range[0], create_time__lte=range[1])
    sum = 0
    count = 0
    for retail in retail_data:
        sum += retail.money - retail.give
        count += 1
    dic["sales"] = sum
    dic["orders"] = count

    ## get product
    item_data = AbpItem.objects.all().aggregate(Count("itemid"))
    dic["products"] = item_data["itemid__count"]

    ## get user
    user_data = AbpUser.objects.filter(regtime__gte=range[0], regtime__lte=range[1]).aggregate(Count("uid"))
    dic["members"] = user_data["uid__count"]


    return render(request, "dashboard.html", dic, context_instance=RequestContext(request, processors=[custom_context]))


def time_range(date1, date2):
    return [time.mktime(date1.timetuple()) - 28800 , time.mktime(date2.timetuple()) - 28800]