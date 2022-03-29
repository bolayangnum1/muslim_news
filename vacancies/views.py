from rest_framework.viewsets import ModelViewSet
from .serializers import VacanciesSerializer, RegistrationSerializer
from .models import Vacancy, Registration
from rest_framework import generics


class VacanciesViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacanciesSerializer
    lookup_field = 'id'


class VacanciesCreate(generics.CreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacanciesSerializer
    lookup_field = 'id'


class VacanciesList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacanciesSerializer
    lookup_field = 'id'


class VacanciesUpdate(generics.UpdateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacanciesSerializer
    lookup_field = 'id'


class VacanciesDelete(generics.DestroyAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacanciesSerializer
    lookup_field = 'id'


class VacanciesDetail(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacanciesSerializer
    lookup_field = 'id'


class RegistrationCreate(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class RegistrationList(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class RegistrationUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class RegistrationDetail(generics.RetrieveAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
