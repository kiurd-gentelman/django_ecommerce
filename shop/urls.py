from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='shop.index'),
    path('/cart', views.cartIndex, name='shop.cart'),
    path('/cart/<id>', views.addToCart, name='shop.cart'),
]
