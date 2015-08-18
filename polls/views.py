from django.shortcuts import render,redirect
from polls.models import User
import json
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

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

def graph_data(request):
	json_data = open('/home/hyeonju/workspace/ginseng/polls/templates/mydata.json').read()
	return HttpResponse(json.dumps(json_data), content_type='application/json')

def test_data(request):
	j_data = open('/home/hyeonju/workspace/ginseng/polls/templates/mydata.json').read()
	return HttpResponse(json.dumps(j_data), content_type='application/json')
