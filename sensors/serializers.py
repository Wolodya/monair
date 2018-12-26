from rest_framework import serializers
from sensors.models import Sensor

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id','sensor_id','date','temperature','humidity','pressure','pm10','pm25','nco','nso2','no3','nnh3','nno2')