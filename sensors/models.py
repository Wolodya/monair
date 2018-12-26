from django.db import models

# Create your models here.
class Sensor(models.Model):
    sensor_id = models.IntegerField()
    date = models.DateTimeField()
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    pm10 = models.IntegerField()
    pm25 = models.IntegerField()
    nco = models.IntegerField()
    nso2 = models.IntegerField()
    no3 = models.IntegerField()
    nnh3 = models.IntegerField()
    nno2 = models.IntegerField()
   