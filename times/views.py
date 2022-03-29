from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Location, Time
from .serializers import LocationSerializer, TimeSerializer


class LocationMVC(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'id'


class TimeMVC(ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    lookup_field = 'date'

    def list(self, request, *args, **kwargs):
        serializer = TimeSerializer(Time.objects.all(), many=True)
        location_id = self.request.query_params['location']

        if location_id:
            serializer = TimeSerializer(Time.objects.filter(location_id=location_id), many=True)

        return Response(serializer.data, status=200)
