from django.urls import path
from .views import VacanciesViewSet, RegistrationList, RegistrationDetail, RegistrationUpdateDelete, RegistrationCreate,\
    VacanciesDelete, VacanciesDetail, VacanciesCreate, VacanciesUpdate, VacanciesList

urlpatterns = [
    path('registration-create/', RegistrationCreate.as_view()),
    path('registration-list/', RegistrationList.as_view()),
    path('registration-detail/<int:pk>/', RegistrationDetail.as_view()),
    path('registration-delete-update/<int:pk>/', RegistrationUpdateDelete.as_view()),

    path('vacancies-create/', VacanciesCreate.as_view()),
    path('vacancies-list/', VacanciesList.as_view()),
    path('vacancies-update/<int:pk>/', VacanciesUpdate.as_view()),
    path('vacancies-delete/<int:pk>/', VacanciesDelete.as_view()),
    path('vacancies-detail/<int:pk>/', VacanciesDetail.as_view())
]