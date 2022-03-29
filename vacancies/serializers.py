from rest_framework import serializers

from vacancies.models import Vacancy


class VacanciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = '__all__'


class CreateVacanciesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, required=True)
    company = serializers.CharField(max_length=200, required=True)
    requirements = serializers.CharField(max_length=2000, required=True)
    salary = serializers.IntegerField(required=True)
    duties = serializers.CharField(max_length=2000, required=True)
    conditions = serializers.CharField(max_length=2000, required=True)
