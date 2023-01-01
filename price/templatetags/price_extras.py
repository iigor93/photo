from django import template

register = template.Library()


@register.filter(name='add_zero')
def add_zero(value):
    return "0" + str(value) if value < 10 else value
