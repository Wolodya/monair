from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from sensors.models import Sensor, SensorIntegerField
from sensors.serializers import SensorSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from sensors.filters import SensorFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from _datetime import datetime, timedelta
from django.db.models.aggregates import Avg
from _collections import defaultdict


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = SensorFilter
    ordering_fields = ('date',)


class SensorIdLocationList(APIView):
    def get(self, request):
        return Response(Sensor.objects.values('sensor_id', 'longitude', 'latitude').distinct())


class Sensor24Hours(APIView):
    def get(self, request, sensor_id):
        now = datetime.now().replace(microsecond=0, second=0, minute=0)
        from_date = now if self.request.GET.get('date') is None else datetime.strptime(self.request.GET.get('date'), '%Y-%m-%d')
        from_date = now if from_date.date() == now.date() else from_date
        fields = [field.name for field in getattr(Sensor, '_meta').get_fields()
                  if isinstance(field, SensorIntegerField)]

        data = {}
        for x in range(1, 25):
            hour = from_date + timedelta(hours=x)
            sensor = Sensor.objects.filter(sensor_id=sensor_id,
                                           date__gte=hour,
                                           date__lt=hour + timedelta(hours=1))
            data[str(hour)] = sensor.aggregate(*[Avg(x) for x in fields])
        data_by_attribute = defaultdict(dict)
        for date, attrs in data.items():
            for attr, value in attrs.items():
                data_by_attribute[attr.split('_')[0]].update({date: value})
        return Response({'from_date': str(from_date - timedelta(days=1)),
                         'from_date': str(from_date),
                         '24h': data_by_attribute})
