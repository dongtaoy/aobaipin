from django.shortcuts import render
from django.template import RequestContext
from abpmodels.models import AbpErpShop, AbpErpRetail
from django.db.models import Avg, Count, Sum
from aobaipin.views import custom_context
import datetime


def shop_comparison(request):
    shop_data = AbpErpShop.objects.all()
    return render(request, "shop_comparison.html", {"select": shop_data},
                  context_instance=RequestContext(request, processors=[custom_context]))


def shop_analysis(request, shopid=1):
    #start = datetime.datetime.strptime("2014/04/29", "%Y/%m/%d")
    shop_data = AbpErpShop.objects.all()
    shop_name = AbpErpShop.objects.get(shopid=shopid).shopname
    avg_sale = get_avg_sale(shopid)
    daily_sale = get_daily_sale(shopid)
    daily_reatil = get_daily_retail(shopid)
    return render(request, "shop_analysis.html", {"dropdowns": shop_data, "shopname": shop_name, "shopid":shopid,
                                                  "avg_sale": avg_sale, "daily_sale": daily_sale, "daily_retail": daily_reatil},
                  context_instance=RequestContext(request, processors=[custom_context]))


def get_avg_sale(shopid):
    return int(AbpErpRetail.objects.filter(shopid=shopid).aggregate(Avg('total'))["total__avg"])


def get_daily_sale(shopid):
    start = datetime.datetime.fromtimestamp(AbpErpShop.objects.get(shopid=shopid).create_time)
    end = datetime.datetime.now()
    return int(((AbpErpRetail.objects.filter(shopid=shopid).aggregate(Sum('total'))["total__sum"]) /
                (end - start).days))


def get_daily_retail(shopid):
    start = datetime.datetime.fromtimestamp(AbpErpShop.objects.get(shopid=shopid).create_time)
    end = datetime.datetime.now()
    return int(((AbpErpRetail.objects.filter(shopid=shopid).aggregate(Count('retailid'))["retailid__count"]) /
                (end - start).days))

