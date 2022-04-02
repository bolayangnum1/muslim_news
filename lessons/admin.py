from django.contrib import admin
from .models import *


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'category']
    search_fields = ['name', 'author', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Lesson, LessonAdmin)
