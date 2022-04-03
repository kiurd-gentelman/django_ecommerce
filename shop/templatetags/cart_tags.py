from django import template
from django.http import HttpResponse

from ..models import Cart

register = template.Library()


@register.simple_tag
def cart_item_count():
    return Cart.objects.count()


@register.inclusion_tag("cart_drawer.html")
def cart_drawer():
    return {"cart": Cart.objects.all()}
