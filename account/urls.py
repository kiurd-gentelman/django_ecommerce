from django.urls import path
from . import views

urlpatterns = [
    path('/login/', views.loginView),
    path('/authentication/', views.authentication, name='shop.authentication'),
]
