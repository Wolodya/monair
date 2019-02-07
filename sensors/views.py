from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from sensors.models import Sensor
from sensors.serializers import SensorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from sensors.filters import SensorFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    ordering_fields = ('date',)

class SensorIdList(APIView):
    def get(self, request):
        ids = Sensor.objects.values_list('sensor_id', flat=True).distinct()
        return Response(ids)
