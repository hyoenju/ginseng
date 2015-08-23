import requests

payload = {'temperature': '11.0', 'humidity': '22.2',\
			'soil_humidity':'11.0', 'sensor_id':'1', 'illumination':'13.4' }
r = requests.post("http://localhost:8000/sensordata/", json=payload)
print r.text
print r.status_code


