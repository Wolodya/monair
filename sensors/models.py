from django.db import models

# Create your models here.
class SensorIntegerField(models.IntegerField):
    def __init__(self, low_limit, up_limit, *args, **kwargs):
        self.low_limit = low_limit
        self.up_limit = up_limit
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["low_limit"] = self.low_limit
        kwargs["up_limit"] = self.up_limit
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if value < self.low_limit:
            value = self.low_limit
        elif value > self.up_limit:
            value = self.up_limit

        setattr(model_instance, self.attname, value)
        return value


class Sensor(models.Model):
    sensor_id = models.IntegerField()
    date = models.DateTimeField()

    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)

    temperature = SensorIntegerField(low_limit=-6000, up_limit=6000)
    humidity = SensorIntegerField(low_limit=0, up_limit=100)
    pressure = SensorIntegerField(low_limit=900000, up_limit=1200000)
    pm10 = SensorIntegerField(low_limit=0, up_limit=500)
    pm25 = SensorIntegerField(low_limit=0, up_limit=500)
    pm1 = SensorIntegerField(low_limit=0, up_limit=500)
    nco = SensorIntegerField(low_limit=0, up_limit=1000)
    nso2 = SensorIntegerField(low_limit=0, up_limit=1000)
    no3 = SensorIntegerField(low_limit=0, up_limit=1000)
    nnh3 = SensorIntegerField(low_limit=0, up_limit=1000)
    nno2 = SensorIntegerField(low_limit=0, up_limit=1000)
