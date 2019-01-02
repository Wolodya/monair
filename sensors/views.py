from django.shortcuts import render
from rest_framework import viewsets, generics
from sensors.models import Sensor
from sensors.serializers import SensorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from sensors.filters import SensorFilter
# Create your views here.


class SensorList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SensorFilter


class SensorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
