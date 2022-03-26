from django.db import models
from django.contrib import admin


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)
    image = models.ImageField(upload_to='category/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
