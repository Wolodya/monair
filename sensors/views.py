from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from sensors.models import Sensor
from sensors.serializers import SensorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from sensors.filters import SensorFilter
from rest_framework.response import Response
# Create your views here.


class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = SensorFilter
    ordering_fields = ('date', 'temperature', 'humidity',
                       'pressure', 'pm10', 'pm25', 'pm1', 'nco', 'nso2', 'no3', 'nnh3', 'nno2')
    ordering=('id',)

class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorIdList(APIView):
    def get(self, request):
        ids = Sensor.objects.values_list('sensor_id', flat=True).distinct()
        return Response(ids)
