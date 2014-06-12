# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Count
from models.models import AbpErpAdmin, AbpErpRetail, AbpItem, AbpUser
from django.template import RequestContext
from hashlib import md5
import time
import datetime
from django_ajax.decorators import ajax

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
        return render(request, "login.html", {"login_fail": 1})


def logout(request):
    try:
        del request.session["uname"]
        del request.session["name"]
        del request.session["u_id"]
    except:
        pass
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
        "uname" : request.session["uname"],
        "username": request.session["name"]
    }


@ajax
def graph_spline(request):
    date = []
    data = []
    start = datetime.date.today() - datetime.timedelta(days=int(request.GET["days"]))
    for i in range(0, int(request.GET["days"]) + 1):
        date.append((start + datetime.timedelta(days=i)).strftime("%y,%m,%d"))
        data.append(str(get_sale_data(time_range((start + datetime.timedelta(days=i)),
                                                 (start + datetime.timedelta(days=i+1))))[0]))
    return [date[0], data]




def dashboard(request):
    if not(login_status(request)):
        return redirect("/login")
    ## sales, members, orders, products
    today = datetime.date.today()
    tom = datetime.date.today() + datetime.timedelta(days=1)
    ## get sales and orders
    dic = {}
    range = time_range(today, tom)
    dic["sales"], dic["orders"] = get_sale_data(range)
    ## get product
    item_data = AbpItem.objects.all().aggregate(Count("itemid"))
    dic["products"] = item_data["itemid__count"]

    ## get user
    user_data = AbpUser.objects.filter(regtime__gte=range[0], regtime__lte=range[1]).aggregate(Count("uid"))
    dic["members"] = user_data["uid__count"]

    return render(request, "dashboard.html", dic, context_instance=RequestContext(request, processors=[custom_context]))


def lock(request):
    if request.method == "GET":
        try:
            del request.session["u_id"]
        except:
            pass

    return render(request, "lockscreen.html", {}, context_instance=RequestContext(request, processors=[custom_context]))


def time_range(date1, date2):
    return [time.mktime(date1.timetuple()), time.mktime(date2.timetuple())]


def get_sale_data(range):
    sum = 0
    count = 0
    retail_data = AbpErpRetail.objects.filter(create_time__gte=range[0], create_time__lte=range[1])
    for retail in retail_data:
        sum += retail.money - retail.give
        count += 1

    return sum, count

