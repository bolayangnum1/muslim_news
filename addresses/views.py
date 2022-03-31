from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import Category, Mosque, MosqueRoom, Madrasah, MosqueCollege, MosqueUniversity, MosqueLibrary
from .serializers import (
    CategorySerializer,
    MosqueSerializer,
    MosqueRoomSerializer,
    MadrasahSerializer,
    MosqueCollegeSerializer,
    MosqueLibrarySerializer, MosqueUniversitySerializer
)


class CategoryMVC(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class MosqueMVC(ModelViewSet):
    queryset = Mosque.objects.all()
    serializer_class = MosqueSerializer
    lookup_field = 'id'


class MosqueRoomMVC(ModelViewSet):
    queryset = MosqueRoom.objects.all()
    serializer_class = MosqueRoomSerializer
    lookup_field = 'id'


class MadrasahMVC(ModelViewSet):
    queryset = Madrasah.objects.all()
    serializer_class = MadrasahSerializer
    lookup_field = 'id'


class MosqueCollegeMVC(ModelViewSet):
    queryset = MosqueCollege.objects.all()
    serializer_class = MosqueCollegeSerializer
    lookup_field = 'id'


class MosqueUniversityMVC(ModelViewSet):
    queryset = MosqueUniversity.objects.all()
    serializer_class = MosqueUniversity
    lookup_field = 'id'



class MosqueLibraryMVC(ModelViewSet):
    queryset = MosqueLibrary.objects.all()
    serializer_class = MosqueLibrarySerializer
    lookup_field = 'id'


class MuslimCreateView(generics.CreateAPIView):
    queryset = MosqueUniversity.objects.all()
    serializer_class = MosqueUniversitySerializer


class MuslimListView(generics.ListAPIView):
    queryset = MosqueUniversity.objects.all()
    serializer_class = MosqueUniversitySerializer


class MuslimUpdateView(generics.UpdateAPIView):
    queryset = MosqueUniversity.objects.all()
    serializer_class = MosqueUniversitySerializer


class MuslimDeleteView(generics.DestroyAPIView):
    queryset = MosqueUniversity.objects.all()
    serializer_class = MosqueUniversitySerializer


class MuslimDetailView(generics.RetrieveAPIView):
    queryset = MosqueUniversity.objects.all()
    serializer_class = MosqueUniversitySerializer