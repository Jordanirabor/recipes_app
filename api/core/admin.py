# core/admin.py

from django.contrib import admin
from .models import Recipe  # add this
# Register your models here.

admin.site.register(Recipe) # add this