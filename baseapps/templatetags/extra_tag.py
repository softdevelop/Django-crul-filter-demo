from django import template
from datetime import timedelta
from baseapps.models import User
register = template.Library()

@register.filter(name='verbose_name')
def verbose_name(value):
    return value

@register.filter(name='view_sex')
def view_sex(value):
    return dict(User.CONST_SEX)[int(value)]

@register.filter(name='order_by')
def order_by(value,arg):
    if not value:
        return arg
    value = value.split(",")
    temp = '-'+arg
    if arg in value:
        value.remove(arg)
        value.append(temp)
    elif temp in value:
        value.remove(temp)
    elif arg not in value:
        value.append(arg)
    return ','.join(value)

@register.filter(name='replace_path')
def replace_path(value,arg):
    start = value.find(arg)
    if arg == 'age':
        value = value[:start] 
    if arg == 'sex':
        end = value.find('&',start)
        temp=""
        if not end is -1:
            temp = value[end:]
        value = value[:start-1]+ temp
    return value