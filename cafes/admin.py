from django.contrib import admin
from .models import Category, Cafe, Restaurant, Magazine, FastFood


admin.site.register(Category)
admin.site.register(Cafe)
admin.site.register(Restaurant)
admin.site.register(Magazine)
admin.site.register(FastFood)