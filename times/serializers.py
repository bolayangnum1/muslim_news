from rest_framework.serializers import ModelSerializer, SerializerMethodField, Serializer

from .models import Location, Time


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = ('id', 'location')


class TimeSerializer(ModelSerializer, Serializer):

    class Meta:
        model = Time
        fields = (
            'id',
            'first_time',
            'second_time',
            'third_time',
            'fourth_time',
            'fifth_time',
            'sixth_time',
            'date',
            'location'
        )
