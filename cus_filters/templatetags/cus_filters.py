from django import template

register = template.Library()


@register.filter(name='div')
def divide(value, arg):
    return float(value) / float(arg)


@register.filter(name='mul')
def multiply(value, arg):
    return float(value) * float(arg)