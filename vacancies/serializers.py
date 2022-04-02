from abc import ABC

from rest_framework import serializers
from vacancies.models import Vacancy, Registration


class VacanciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = '__all__'


class RegistrationSerializer(serializers.Serializer):

    class Meta:
        model = Registration
        fields = '__all__'
