from django.shortcuts import render, render_to_response
from django.views import generic
from .models import Diary
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User



def logina(request):#登录页面
	return render(request, 'diaries/login.html')


def login(request):#登录验证方法
	if request.method == 'POST':
		print('我执行了')
		username = request.POST.get('name','')
		password = request.POST.get('password','')
		user = authenticate(username=username,password=password)
		if user and user.is_active:
			auth.login(request, user)
			request.session['username']=username
			print('dengluchenggong')

	return HttpResponseRedirect('/diary/')

def index(request):
	all_diaries = Diary.objects.all()
	if request.session.get('username'):
		username = request.session["username"]
	else:
		username = ''
	return render_to_response('diaries/index.html',{'username':username,'all_diaries':all_diaries})

def logout(request):
	del request.session["username"]
	return HttpResponseRedirect('/diary/')