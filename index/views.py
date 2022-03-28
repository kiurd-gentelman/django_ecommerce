from django.shortcuts import render


# Create your views here.
from shop.models import Cart


def index(request):
    carts = Cart.objects.all()
    return render(request, 'index/index.html', {'carts': carts})
