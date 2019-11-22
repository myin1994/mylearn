from django import template

register = template.Library()

@register.inclusion_tag("left_menu.html")
def left_menu(i):
    return {"data":i}