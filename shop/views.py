from django.contrib.auth.decorators import login_required
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


@login_required(login_url='/account/login/')
def addToCart(request, id):
    product = Product.objects.get(id=id)
    cart = Cart.objects.create(product_id=id, quantity=1, price=product.price, user_id=0)
    return redirect('shop.index')


def cartIndex(request):
    cart = Cart.objects.all()
    return render(request, 'cart/index.html', {'cart': cart})