from django.urls import path
from .views import VacanciesViewSet, RegistrationList, RegistrationDetail, RegistrationUpdateDelete, RegistrationCreate,\
    VacanciesDelete, VacanciesDetail, VacanciesCreate, VacanciesUpdate, VacanciesList

urlpatterns = [
    # path('vacancies/', VacanciesViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('vacancy/<int:id>/', VacanciesViewSet.as_view({'get': 'retrieve'})),

    path('registration/', RegistrationCreate.as_view()),
    path('registration/', RegistrationList.as_view()),
    path('registration/<int:pk>/', RegistrationDetail.as_view()),
    path('registration/<int:pk>/', RegistrationUpdateDelete.as_view()),

    path('vacancies/', VacanciesCreate.as_view()),
    path('vacancies/', VacanciesList.as_view()),
    path('vacancies/<int:pk>/', VacanciesUpdate.as_view()),
    path('vacancies/<int:pk>/', VacanciesDelete.as_view()),
    path('vacancies/<int:pk>/', VacanciesDetail.as_view())
]