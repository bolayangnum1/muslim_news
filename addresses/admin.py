from django.contrib import admin
from .models import Category, Mosque, MosqueRoom, MosqueCollege, Madrasah, MosqueLibrary, MosqueUniversity

fields = ['name', 'address', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class MosqueAdmin(admin.ModelAdmin):
    list_display = fields
    list_filter = fields
    search_fields = fields


admin.site.register(Category, CategoryAdmin)
admin.site.register(Mosque, MosqueAdmin)
admin.site.register(MosqueRoom, MosqueAdmin)
admin.site.register(MosqueCollege, MosqueAdmin)
admin.site.register(Madrasah, MosqueAdmin)
admin.site.register(MosqueUniversity, MosqueAdmin)
admin.site.register(MosqueLibrary, MosqueAdmin)
