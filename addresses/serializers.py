from rest_framework import serializers

from .models import Category, Mosque, MosqueRoom, MosqueCollege, MosqueUniversity, Madrasah, MosqueLibrary

abstractFields = ('id', 'name', 'address', 'contacts', 'images', 'longitude', 'latitude', 'category')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        ref_name = "Address category serializer"
        model = Category
        fields = ('id', 'name')


class MosqueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mosque
        fields = abstractFields


class MosqueRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MosqueRoom
        fields = (*abstractFields, 'gender')


class MosqueCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MosqueCollege
        fields = abstractFields


class MosqueUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MosqueUniversity
        fields = abstractFields


class MadrasahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Madrasah
        fields = abstractFields


class MosqueLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MosqueLibrary
        fields = (*abstractFields, 'work_time')

