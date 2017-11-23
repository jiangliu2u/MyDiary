from django.shortcuts import render
from django.views import generic
from .models import Diary
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
import django.contrib.auth
from django.contrib.auth.models import User


class IndexView(generic.ListView):
    template_name = 'diaries/index.html'
    context_object_name = 'all_diaries'

    def get_queryset(self):
        return Diary.objects.all()


class DetailView(generic.DetailView):
    model = Diary
    template_name = 'diaries/detail.html'

    def get_queryset(self):
        return Diary.objects.all()


def logina(request):
	return render(request, 'diaries/login.html')

def login(request):
	if request.method == 'POST':
		print('我执行了')
		username = request.POST.get('name','')
		password = request.POST.get('password','')
		user = authenticate(username=username,password=password)
		if user and user.is_active:
			auth.login(request, user)
			print('dengluchenggong')
		
		return HttpResponseRedirect('/diary/')