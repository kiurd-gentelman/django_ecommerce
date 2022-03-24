from django.db import models
from django.contrib import admin


# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='team/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'created_at', 'updated_at')
