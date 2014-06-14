from django_ajax.decorators import ajax
from aobaipin.views import get_sale_data, time_range
from abpmodels.models import AbpErpShop
from django.template.loader import get_template
from django.template import Context
from analysis.views import get_daily_retail, get_avg_sale, get_daily_sale
import datetime
import json

@ajax
def ajax_graph(request):
    start = datetime.datetime.strptime(str(request.GET["start"]), "%Y/%m/%d")
    end = datetime.datetime.strptime(str(request.GET["end"]), "%Y/%m/%d")
    shopids = list(set(json.loads(request.GET["shopid"])))
    data = []
    daily_retail = []
    daily_sale = []
    avg_sale = []
    shopname = []
    for shopid in shopids:
        dic = {}
        arr = []
        for i in range(0, (end - start).days + 1):
            arr.append(float(get_sale_data(time_range((start + datetime.timedelta(days=i)),
                                                    (start + datetime.timedelta(days=i + 1))), shopid)[0]))
        dic["name"] = AbpErpShop.objects.get(shopid=shopid).shopname
        dic["data"] = arr
        data.append(dic)
        shopname.append(dic["name"])
        daily_retail.append(get_daily_retail(shopid))
        daily_sale.append(get_daily_sale(shopid))
        avg_sale.append(get_avg_sale(shopid))

    t = get_template("shop_comparison_table.html")
    html = t.render(Context({
        'shopname': shopname,
        'daily_retail': daily_retail,
        'daily_sale': daily_sale,
        'avg_sale': avg_sale
    }))

    return [map(int, start.strftime("%y,%m,%d").split(',')), data, html]