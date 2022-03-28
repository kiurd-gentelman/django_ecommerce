from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Product, Category, Brand, Cart
from pprint import pprint


# Create your views here.

def index(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'shop/index.html', {'brands': brands, 'categories': categories, 'products': products})


def addToCart(request, id):
    product = Product.objects.get(id=id)
    cart = Cart.objects.create (product_id=id, quantity=1,price=product.price, user_id=0)
    return redirect('shop.index')
