from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def hello(request):
    t = get_template("base.html")
    html = t.render(Context())
    return HttpResponse(html)

def world(request):
    return HttpResponse("World")