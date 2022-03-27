from django.shortcuts import render

from .models import Product, Category, Brand
from pprint import pprint


# Create your views here.

def index(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'shop/index.html', {'brands': brands, 'categories': categories, 'products': products})
