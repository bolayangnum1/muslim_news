from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer, CafesSerializer, RestaurantSerializer, MagazineSerializer, FastFoodSerializer
from .models import Category, MosqueCafe, Restaurant, Magazine, FastFood
from rest_framework import generics

class CategoryMVC(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class CafesMVC(ModelViewSet):
    queryset = MosqueCafe.objects.all()
    serializer_class = CafesSerializer
    lookup_field = 'id'


class RestaurantMVC(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'


class MagazineMVC(ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer
    lookup_field = 'id'


class FastFoodMVC(ModelViewSet):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer
    lookup_field = 'id'


class MosqueCafeCreateView(generics.CreateAPIView):
    queryset = MosqueCafe.objects.all()
    serializer_class = CafesSerializer
    lookup_field = 'id'


class MosqueCafeListView(generics.ListAPIView):
    queryset = MosqueCafe.objects.all()
    serializer_class = CafesSerializer
    lookup_field = 'id'


class MosqueCafeDeleteView(generics.DestroyAPIView):
    queryset = MosqueCafe.objects.all()
    serializer_class = CafesSerializer
    lookup_field = 'id'


class MosqueCafeUpdateView(generics.UpdateAPIView):
    queryset = MosqueCafe.objects.all()
    serializer_class = CafesSerializer
    lookup_field = 'id'


class MosqueCafeDetailView(generics.RetrieveAPIView):
    queryset = MosqueCafe.objects.all()
    serializer_class = CafesSerializer
    lookup_field = 'id'
