from rest_framework import serializers
from .models import *



abstractFields = ('id', 'name', 'certificate', 'mosqueRoom', 'contacts', 'address', 'images')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "Cafe category serializer"
        model = Category
        fields = ('id', 'name')


class CafesSerializer(serializers.ModelSerializer):

    class Meta:
        model = MosqueCafe
        fields = abstractFields


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (*abstractFields, 'bigHall')


class MagazineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Magazine
        fields = (*abstractFields, 'site', 'alcohol', 'productsCertificate', 'site')


class FastFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = FastFood
        fields = (*abstractFields, 'workTime', 'site')
