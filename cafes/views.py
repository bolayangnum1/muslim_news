from .serializers import CafesSerializer, RestaurantSerializer, MagazineSerializer, FastFoodSerializer, \
    CategorySerializer
from .models import Cafe, Restaurant, Magazine, FastFood, Category
from rest_framework import generics


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDeleteView(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryUpdateView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CafeCreateView(generics.CreateAPIView):
    queryset = Cafe.objects.filter(is_published=True)
    serializer_class = CafesSerializer


class CafeListView(generics.ListAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafesSerializer


class CafeDeleteView(generics.DestroyAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafesSerializer


class CafeUpdateView(generics.UpdateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafesSerializer


class CafeDetailView(generics.RetrieveAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafesSerializer


class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.filter(is_published=True)
    serializer_class = RestaurantSerializer


class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantUpdateView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDeleteView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MagazineCreateView(generics.CreateAPIView):
    queryset = Magazine.objects.filter(is_published=True)
    serializer_class = MagazineSerializer


class MagazinListView(generics.ListAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer


class MagazineUpdateView(generics.UpdateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer


class MagazineDeleteView(generics.DestroyAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer


class MagazineDetailView(generics.RetrieveAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer


class FastFoodCreateView(generics.CreateAPIView):
    queryset = FastFood.objects.filter(is_published=True)
    serializer_class = FastFoodSerializer


class FastFoodListView(generics.ListAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer


class FastFoodUpdateView(generics.UpdateAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer


class FastFoodDeleteView(generics.DestroyAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer


class FastFoodDetailView(generics.RetrieveAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer