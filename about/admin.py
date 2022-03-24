from django.contrib import admin

# Register your models here.
from .models import About, AboutAdmin

admin.site.register(About, AboutAdmin)
