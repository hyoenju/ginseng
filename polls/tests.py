from django.test import TestCase, Client
from polls.models import SensorData

class SensorDataTestCase(TestCase):
	
	def test_insert_new_sensor_data(self):
		tem = 29.7
		hum = 12.3
		s_m = 14.3
		illu = 22.3
		sensor_id = 1

		data = SensorData.objects.create(\
				sensor_id = sensor_id,
				temperature = tem,
				humidity = hum,
				soil_humidity = s_m,
				illumination = illu)
		pass



