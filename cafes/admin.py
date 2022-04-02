from django.contrib import admin
from .models import Category, Cafe, Restaurant, Magazine, FastFood


restaurantfields = ['name', 'bighall', 'certificate', 'mosqueroom', 'address', 'category', 'is_published']
cafefields = ['name', 'certificate', 'mosqueroom', 'address', 'category', 'is_published']
magazinefields = ['name', 'alcohol', 'productsCertificate', 'worktime', 'certificate', 'mosqueroom', 'address', 'category', 'is_published']
fastfoodfields = ['name', 'worktime', 'certificate', 'mosqueroom', 'address', 'category', 'is_published']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']


class CafeAdmin(admin.ModelAdmin):
    list_display = cafefields
    list_filter = cafefields
    search_fields = cafefields


class RestaurantAdmin(admin.ModelAdmin):
    list_display = restaurantfields
    list_filter = restaurantfields
    search_fields = restaurantfields


class MagazineAdmin(admin.ModelAdmin):
    list_display = magazinefields
    list_filter = magazinefields
    search_fields = magazinefields


class FastFoodAdmin(admin.ModelAdmin):
    list_display = fastfoodfields
    list_filter = fastfoodfields
    search_fields = fastfoodfields


admin.site.register(Category, CategoryAdmin)
admin.site.register(Cafe, CafeAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Magazine, MagazineAdmin)
admin.site.register(FastFood, FastFoodAdmin)
