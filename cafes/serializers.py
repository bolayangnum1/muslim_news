from rest_framework import serializers
from .models import *


class CafesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cafe
        fields = ('name', 'certificate', 'mosqueroom', 'contacts', 'address', 'images', 'longitude', 'latitude', 'category')


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('name', 'bighall', 'certificate', 'mosqueroom', 'contacts', 'address', 'images', 'longitude', 'latitude', 'category')


class MagazineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Magazine
        fields = '__all__'


class FastFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = FastFood
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    categorycafe = CafesSerializer(many=True)
    categoryfastfoot = FastFoodSerializer(many=True)
    categorymagazine = MagazineSerializer(many=True)
    categoryrestarant = RestaurantSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'

