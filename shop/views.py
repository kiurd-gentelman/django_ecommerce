from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pdb

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
    cart = Cart.objects.filter(user=request.user, product=product)
    if cart.exists():
        # return HttpResponse(cart.quantity)
        cart = cart.first()
        cart.quantity = cart.quantity + 1
        cart.save()
    else:
        Cart.objects.create(product_id=id, quantity=1, price=product.price, user_id=1)
    return redirect('shop.index')


@login_required(login_url='/account/login/')
def cartIndex(request):
    cart = Cart.objects.all()
    return render(request, 'cart/index.html', {'cart': cart})
