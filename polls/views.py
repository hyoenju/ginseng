from django.shortcuts import render,redirect
from polls.models import User, SensorData
from polls.models import SensorData as SensorData_model 
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json
from time import strftime, strptime
from datetime import datetime, timedelta

def home(request):
	return render(request, 'home.html')

def index(request):
	return render(request, 'index.html')

def login_data(request):
	user= list(User.objects.values())	
	return HttpResponse(json.dumps(user), content_type='application/json')

def login(request):
	if request.method == "POST":
		user_id = request.POST['user_username']
		request.session['user_id'] = user_id
		session_id=request.session.get('user_id')
		return redirect(reverse_lazy('home'))

def logout(request):
	del request.session['user_id']
	session_id=str(request.session.get('user_id'))
	return redirect(reverse_lazy('home'))

def administer(request):
	if (request.session.get('user_id') is None):
		return redirect(reverse_lazy('home'))
	else:
		Sensor1_date=SensorData_model.objects.filter(sensor_id=1).values('created_at')
		date_count_1=(Sensor1_date.count())-1
		last_date_1=str(Sensor1_date[date_count_1]['created_at']+timedelta(hours=9))
		
		Sensor2_date=SensorData_model.objects.filter(sensor_id=2).values('created_at')
		date_count_2=(Sensor2_date.count())-1
		last_date_2=str(Sensor2_date[date_count_2]['created_at']+timedelta(hours=9))
		
		Sensor3_date=SensorData_model.objects.filter(sensor_id=3).values('created_at')
		date_count_3=(Sensor3_date.count())-1
		last_date_3=str(Sensor3_date[date_count_3]['created_at']+timedelta(hours=9))
		
		Sensor4_date=SensorData_model.objects.filter(sensor_id=4).values('created_at')
		date_count_4=(Sensor4_date.count())-1
		last_date_4=str(Sensor4_date[date_count_4]['created_at']+timedelta(hours=9))
		
		return render(request, 'administer.html', {'sensor_1': last_date_1, 'sensor_2':last_date_2, 'sensor_3':last_date_3 ,'sensor_4':last_date_4})

class SensorData(APIView):
	def post(self, request, format=None):
		temperature = request.data['temperature']
		humidity = request.data['humidity']
		illumination = request.data['illumination']
		soil_humidity = request.data['soil_humidity']
	
		sensor_id= request.data['sensor_id']


		data = SensorData_model.objects.create(\
			temperature = float(temperature),
			humidity = float(humidity),
			illumination = float(illumination),
			soil_humidity = float(soil_humidity),
			sensor_id = int(sensor_id)
			)
		data.save()
		return HttpResponse("{result:Suscces}", content_type='application/json')

def sensor1_data(request):
	sensor1_list=list(
		SensorData_model.objects.filter(
			sensor_id=1).values(
				'temperature','humidity','illumination','soil_humidity', 'id', 'created_at'))

	total_count = len(sensor1_list)
	sensor1_list = sensor1_list[total_count-2000:]
	sensor1_data = [] 
	for sensor1_object in sensor1_list:
		time_data = sensor1_object['created_at'].strftime('%Y/%m/%d %H:%M:%S')
		sensor1_object['created_at'] = time_data 
		sensor1_data.append(sensor1_object)

	return HttpResponse(json.dumps(sensor1_data), content_type='application/json')

def sensor2_data(request):
	sensor2_list=list(
		SensorData_model.objects.filter(
			sensor_id=2).values(
				'temperature','humidity','illumination','soil_humidity', 'id', 'created_at'))

	total_count = len(sensor2_list)
	sensor2_list = sensor2_list[total_count-2000:]
	sensor2_data = [] 
	for sensor2_object in sensor2_list:
		time_data = sensor2_object['created_at'].strftime('%Y/%m/%d %H:%M:%S')
		sensor2_object['created_at'] = time_data 
		sensor2_data.append(sensor2_object)

	return HttpResponse(json.dumps(sensor2_data), content_type='application/json')

def sensor3_data(request):
	sensor3_list=list(
		SensorData_model.objects.filter(
			sensor_id=3).values(
				'temperature','humidity','illumination','soil_humidity', 'id', 'created_at'))

	total_count = len(sensor3_list)
	sensor3_list = sensor3_list[total_count-2000:]
	sensor3_data = [] 
	for sensor3_object in sensor3_list:
		time_data = sensor3_object['created_at'].strftime('%Y/%m/%d %H:%M:%S')
		sensor3_object['created_at'] = time_data 
		sensor3_data.append(sensor3_object)

	return HttpResponse(json.dumps(sensor3_data), content_type='application/json')

def sensor4_data(request):
	sensor4_list=list(
		SensorData_model.objects.filter(
			sensor_id=4).values(
				'temperature','humidity','illumination','soil_humidity', 'id', 'created_at'))

	total_count = len(sensor4_list)
	sensor4_list = sensor4_list[total_count-2000:]
	sensor4_data = [] 
	for sensor4_object in sensor4_list:
		time_data = sensor4_object['created_at'].strftime('%Y/%m/%d %H:%M:%S')
		sensor4_object['created_at'] = time_data 
		sensor4_data.append(sensor4_object)

	return HttpResponse(json.dumps(sensor4_data), content_type='application/json')

def update_sensor(request):
	selected_option = request.GET.get("x_value")
	id_1=1
	id_2=4
	sensor_date=list(SensorData_model.objects.values('humidity','temperature','soil_humidity','illumination'))
	return HttpResponse(json.dumps(sensor_date), content_type='application/json')

def check_status(request):
	sensor = request.GET.get('sensor_name')
	sensor_id=0
	if sensor == "sensor1":
		sensor_id=1
	elif sensor == "sensor2":
		sensor_id=2
	elif sensor == "sensor3":
		sensor_id=3
	elif sensor == "sensor4":
		sensor_id=4
	Sensor1_date=SensorData_model.objects.filter(sensor_id=sensor_id).values('created_at')
	date_count=(Sensor1_date.count())-1
	last_date=(Sensor1_date[date_count]['created_at']+timedelta(hours=9))
	print (last_date)
	current_date=datetime.now()-timedelta(minutes=-5)
	#current_date=datetime(year=2015, month=8, day=28,hour=20,minute=55,second=00, microsecond=0)
	last_date=last_date.astimezone(timezone.utc).replace(tzinfo=None)
	if current_date<=last_date:
		text=("%s 의 연결이 확인되었습니다." %sensor)
	else:
		text=("%s 이 최소 5분동안 동작하지 않았습니다. 센서를 확인해주세요." %sensor)
	return HttpResponse(text)

def get_selector(request):
	start_date = request.GET.get('startDate')
	end_date = request.GET.get('endDate')
	sensor = request.GET.get('sensor')
	
	print("hi"+sensor)
	start_data = datetime.strptime(start_date[:24].strip(), '%a %b %d %Y %H:%M:%S')
	end_data  = datetime.strptime(end_date[:24].strip(), '%a %b %d %Y %H:%M:%S')

#	sensor_date=list(SensorData_model.objects.values(
#		'humidity','temperature',"soil_humidity","illumination"))
	# YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]
	#print(type(start_data))
	str_start_date = start_data.strftime("%Y-%m-%d %H:%M:%S")
	str_end_date = end_data.strftime("%Y-%m-%d %H:%M:%S")

	sensor_date=(list(SensorData_model.objects.filter(
		created_at__range=(str_start_date, str_end_date)).values(
			'humidity','temperature',"soil_humidity","illumination")))

	#print(sensor_date)


	return HttpResponse(json.dumps(sensor_date), content_type='application/json')
