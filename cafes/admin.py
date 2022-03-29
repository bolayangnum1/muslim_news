from django.contrib import admin
from .models import Category, MosqueCafe, Restaurant, Magazine, FastFood


admin.site.register(Category)
admin.site.register(MosqueCafe)
admin.site.register(Restaurant)
admin.site.register(Magazine)
admin.site.register(FastFood)