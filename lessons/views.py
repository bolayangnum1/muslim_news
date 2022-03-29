from rest_framework.viewsets import ModelViewSet

from .models import Lesson, Category
from .serializers import CategoriesSerializer, LessonsSerializer


class CategoriesView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    lookup_field = 'id'


class LessonsView(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonsSerializer
    lookup_field = 'id'
