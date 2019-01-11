from rest_framework import serializers
from sensors.models import Sensor


class SensorSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['temperature'] = ret['temperature']*0.01

        return ret

    def create(self):
        sensor = Sensor(sensor_id=self.validated_data['sensor_id'],
                        date=self.validated_data['date'],
                        temperature=self.check_limits(
                            self.validated_data['temperature'], -6000, 6000),
                        humidity=self.check_limits(
                            self.validated_data['humidity'], 0, 100),
                        pressure=self.check_limits(
                            self.validated_data['pressure'], 900000, 1200000),
                        pm10=self.check_limits(
                            self.validated_data['pm10'], 0, 500),
                        pm25=self.check_limits(
                            self.validated_data['pm25'], 0, 500),
                        pm1=self.check_limits(
                            self.validated_data['pm1'], 0, 500),
                        nco=self.check_limits(
                            self.validated_data['nco'], 0, 1000),
                        nso2=self.check_limits(
                            self.validated_data['nso2'], 0, 1000),
                        no3=self.check_limits(
                            self.validated_data['no3'], 0, 1000),
                        nnh3=self.check_limits(
                            self.validated_data['nnh3'], 0, 1000),
                        nno2=self.check_limits(self.validated_data['nno2'], 0, 1000))
        sensor.save()
        return sensor

    def update(self, instance, validated_data):
        instance.sensor_id = validated_data['sensor_id']
        instance.date = validated_data['date']
        instance.temperature = self.check_limits(
            validated_data['temperature'], -6000, 6000)
        instance.humidity = self.check_limits(
            validated_data['humidity'], 0, 100)
        instance.pressure = self.check_limits(
            validated_data['pressure'], 900000, 1200000)
        instance.pm10 = self.check_limits(
            validated_data['pm10'], 0, 500)
        instance.pm25 = self.check_limits(
            validated_data['pm25'], 0, 500)
        instance.pm1 = self.check_limits(
            validated_data['pm1'], 0, 500)
        instance.nco = self.check_limits(
            validated_data['nco'], 0, 1000)
        instance.nso2 = self.check_limits(
            validated_data['nso2'], 0, 1000)
        instance.no3 = self.check_limits(
            validated_data['no3'], 0, 1000)
        instance.nnh3 = self.check_limits(
            validated_data['nnh3'], 0, 1000)
        instance.nno2 = self.check_limits(self.validated_data['nno2'], 0, 1000)
        instance.save()
        return instance

    class Meta:
        model = Sensor
        fields = ('id', 'sensor_id', 'date', 'temperature', 'humidity',
                  'pressure', 'pm10', 'pm25', 'pm1', 'nco', 'nso2', 'no3', 'nnh3', 'nno2')

    def check_limits(self, value, low_limit, up_limit):
        if value < low_limit:
            value = low_limit
        elif value > up_limit:
            value = up_limit
        else:
            pass
        return value
