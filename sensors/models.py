from django.db import models

# Create your models here.


class Sensor(models.Model):
    sensor_id = models.IntegerField()
    date = models.DateTimeField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    pm10 = models.IntegerField()
    pm25 = models.IntegerField()
    pm1 = models.IntegerField()
    nco = models.IntegerField()
    nso2 = models.IntegerField()
    no3 = models.IntegerField()
    nnh3 = models.IntegerField()
    nno2 = models.IntegerField()
