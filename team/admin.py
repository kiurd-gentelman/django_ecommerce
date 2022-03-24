from django.contrib import admin

# Register your models here.

from .models import Team ,TeamAdmin


admin.site.register(Team , TeamAdmin)
