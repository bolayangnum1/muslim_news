from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


class VacanciesViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacanciesSerializer
    lookup_field = 'id'
