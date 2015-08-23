from django.db import models

class User(models.Model):
	user = models.CharField(max_length=100, primary_key=True)
	password = models.CharField(max_length=100, primary_key=False)

class SensorData(models.Model):
	sensor_id = models.IntegerField()
	temperature = models.FloatField(null=True, blank=True, default=None) 
	humidity = models.FloatField(null=True, blank=True, default=None)
	illumination = models.FloatField(null=True, blank=True, default=None)
	soil_humidity = models.FloatField(null=True, blank=True, default=None)
	created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
