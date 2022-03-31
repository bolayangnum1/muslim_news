from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "Cafe category serializer"
        model = Category
        fields = '__all__'


class CafesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cafe
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = '__all__'


class MagazineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Magazine
        fields = '__all__'


class FastFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = FastFood
        fields = '__all__'
