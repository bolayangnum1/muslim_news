from rest_framework import serializers
from .models import *


class CafesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cafe
        fields = ('id', 'name', 'certificate', 'mosqueroom', 'contacts', 'address', 'images', 'longitude', 'latitude', 'is_published')


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'bighall', 'certificate', 'mosqueroom', 'contacts', 'address', 'images', 'longitude', 'latitude', 'is_published')


class MagazineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Magazine
        fields = ('name', 'id', 'site', 'alcohol', 'productsCertificate', 'worktime', 'certificate', 'mosqueroom', 'contacts', 'address', 'images', 'longitude', 'latitude', 'is_published')


class FastFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = FastFood
        fields = ('name', 'id', 'worktime', 'site', 'certificate', 'mosqueroom', 'contacts', 'address', 'images', 'longitude', 'latitude', 'is_published')
