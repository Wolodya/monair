from rest_framework import serializers
from sensors.models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['date'] = instance.date.strftime("%Y-%m-%d %H:%M:%S")
        ret['temperature'] = ret['temperature']*0.01
        return ret

    class Meta:
        model = Sensor
        fields = '__all__'
