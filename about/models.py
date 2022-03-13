from django.db import models


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, blank='false')
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
