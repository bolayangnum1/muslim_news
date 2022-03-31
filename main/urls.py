from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vacancies.urls')),
    path('', include('lessons.urls')),
    path('', include('addresses.urls')),
    path('', include('cafes.urls')),
    path('', include('times.urls')),
]
urlpatterns += doc_urls
