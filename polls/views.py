from django.shortcuts import render,redirect
from polls.models import User, SensorData
from polls.models import SensorData as SensorData_model 
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json
from time import strftime
from datetime import datetime

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
		return render(request, 'administer.html')

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
	temperature=list(SensorData_model.objects.filter(sensor_id=sensor_id).values('temperature','humidity','illumination','soil_humidity', 'id'))
	return HttpResponse(json.dumps(temperature), content_type='application/json')

def update_sensor(request):
	id_1=1
	id_2=4
	sensor_date=list(SensorData_model.objects.filter(sensor_id=id_1).values('humidity','temperature'))

	return HttpResponse(json.dumps(sensor_date), content_type='application/json')

def graph_data(request):
	json_data = open('/home/hyeonju/workspace/ginseng/polls/templates/mydata.json').read()
	return HttpResponse(json.dumps(json_data), content_type='application/json')

def get_selector(request):
	selected_option = request.GET('graph_x', None)
	print (selected_option)
	return HttpResponse(selected_option)
