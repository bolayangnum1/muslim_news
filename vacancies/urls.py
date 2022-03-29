from django.urls import path
from .views import *

urlpatterns = [
    path('vacancies/', VacanciesViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('vacancy/<int:id>/', VacanciesViewSet.as_view({'get': 'retrieve'}))
]