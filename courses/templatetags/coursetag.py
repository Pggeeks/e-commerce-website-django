import math

from courses.models import (user_course)
from django import template

register = template.Library()
@register.simple_tag
def sellprice(price,discount):
    if discount is None or discount==0:
        return price
    sellprice = price - (price * discount * 1/100)
    return math.ceil(sellprice)


@register.filter
def symbol(price):
    return f"₹{price}"

@register.simple_tag
def capname(cap_name):
    return f"{cap_name}".capitalize() 

@register.simple_tag
def is_enrolled(request , course):
    if not request.user.is_authenticated:
        return False
        # i you are enrooled in this course you can watch every video
    user = request.user
    try:
        userch = user_course.objects.get(user = user  , course = course)
        return True
    except:
        return False
@register.simple_tag
def lastprice(final,coupondiscount):
    if coupondiscount:
        return math.ceil((final) * coupondiscount * 1/100)
    else:
        return math.ceil(final)

@register.filter(name='times') 
def times(number):
    return range(1,number+1)
