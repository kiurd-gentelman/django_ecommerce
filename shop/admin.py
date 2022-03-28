from django.contrib import admin

# Register your models here.

from .models import Product, Category, Brand, ProductAdmin, Cart

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
