
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('index.urls')),
    path('shop', include('shop.urls')),
    path('about', include('about.urls')),
]
