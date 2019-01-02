from django_filters import rest_framework as filters
from sensors.models import Sensor


class SensorFilter(filters.FilterSet):
    date = filters.DateTimeFromToRangeFilter()
    sensor_id = filters.NumberFilter()

    class Meta:
        model = Sensor
        fields = ['sensor_id', 'date']
