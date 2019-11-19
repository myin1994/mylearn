from django import template

register = template.Library()

@register.filter
def func(v1,v2):#第一个参数是过滤器前的变量
    print(v1,v2)
    return v1 + v2

@register.simple_tag
def tag1(*args):
    print(args)
    return " ".join(args) + 'ootag'

@register.inclusion_tag("leftmenu.html")
def pp(v1,v2):
    return {"data":v1,"data1":v2}