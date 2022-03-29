from rest_framework import serializers

from .models import Category, Lesson


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CategoriesSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'lessons')

    def get_lessons(self, object):
        allLessons = Lesson.objects.filter(category__name=object)
        return LessonsSerializer(allLessons, many=True).data

    def create(self, validated_data):
        category = Category.objects.create(**validated_data)
        return category


class LessonsSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'author', 'audio', 'category')

    def get_category(self, object):
        categoryObject = Category.objects.get(category__name=object)
        return CategorySerializer(categoryObject, many=False).data

    def create(self, validated_data):
        lesson = Lesson.objects.create(**validated_data)
        return lesson