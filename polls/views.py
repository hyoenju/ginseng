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
from time import strftime
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
		last_date_1=str(Sensor1_date[date_count_1]['created_at'])
		
		Sensor2_date=SensorData_model.objects.filter(sensor_id=2).values('created_at')
		date_count_2=(Sensor2_date.count())-1
		last_date_2=str(Sensor2_date[date_count_2]['created_at'])
		
		Sensor3_date=SensorData_model.objects.filter(sensor_id=3).values('created_at')
		date_count_3=(Sensor3_date.count())-1
		last_date_3=str(Sensor3_date[date_count_3]['created_at'])
		
		Sensor4_date=SensorData_model.objects.filter(sensor_id=4).values('created_at')
		date_count_4=(Sensor4_date.count())-1
		last_date_4=str(Sensor4_date[date_count_4]['created_at'])
		
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

def temperature_data(request):
	sensor_id=1
	temperature_list=list(
		SensorData_model.objects.filter(
			sensor_id=sensor_id).values(
				'temperature','humidity','illumination','soil_humidity', 'id', 'created_at'))

	total_count = len(temperature_list)
	temperature_list = temperature_list[total_count-2000:]
	temperature = [] 
	for temperature_object in temperature_list:
		time_data = temperature_object['created_at'].strftime('%Y/%m/%d %H:%M:%S')
		temperature_object['created_at'] = time_data 
		temperature.append(temperature_object)

	return HttpResponse(json.dumps(temperature), content_type='application/json')


def update_sensor(request):
	selected_option = request.GET.get("x_value")
	id_1=1
	id_2=4
	sensor_date=list(SensorData_model.objects.values('humidity','temperature','soil_humidity','illumination'))
	return HttpResponse(json.dumps(sensor_date), content_type='application/json')

def graph_data(request):
	Sensor1_date=SensorData_model.objects.filter(sensor_id=1).values('created_at')
	date_count=(Sensor1_date.count())-1
	last_date=str(Sensor1_date[date_count]['created_at'])
	now_date=datetime.now()
	now_date=now_date.astimezone(timezone.utc).replace(tzinfo=None)
	alert_date=now_date + timedelta(hours=-9)

	return HttpResponse(json.dumps(last_date), content_type='application/json')

def get_selector(request):
	selected_date = request.GET.get('startDate')
	print (type(selected_date))
	sensor_date=(list(SensorData_model.objects.values('humidity','temperature',"soil_humidity","illumination")))
	return HttpResponse(json.dumps(sensor_date), content_type='application/json')
