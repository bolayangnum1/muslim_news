from django.urls import path
from .views import *

urlpatterns = [
    path('categories/', CategoriesView.as_view({'get': 'list', 'post': 'create'})),
    path('lessons/', LessonsView.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<int:id>/', CategoriesView.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('lessons/<int:id>/', LessonsView.as_view({'get': 'retrieve', 'delete': 'destroy'}))
]