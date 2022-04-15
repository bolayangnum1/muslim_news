from django.contrib import admin
from django.urls import path, include
from . import settings
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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)