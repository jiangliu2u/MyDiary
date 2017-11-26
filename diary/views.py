from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic
from .models import Diary
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User


def detail(request, diary_id):  # 详情页面
    diary = get_object_or_404(Diary, pk=diary_id)
    if request.session.get('username'):
        username = request.session["username"]
    else:
        username = ''
    return render(request, 'diaries/detail.html', {'diary': diary, 'username': username})


def logina(request):  # 登录页面
    return render(request, 'diaries/login.html')


def login(request):  # 登录验证方法
    if request.method == 'POST':
        print('我执行了')
        username = request.POST.get('name', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            request.session['username'] = username
            print('dengluchenggong')

    return HttpResponseRedirect('/diary/')


def index(request):
    all_diaries = Diary.objects.order_by('-pub_date')
    if request.session.get('username'):
        username = request.session["username"]
    else:
        username = ''
    return render_to_response('diaries/index.html', {'username': username, 'all_diaries': all_diaries})


def logout(request):
    del request.session["username"]
    return HttpResponseRedirect('/diary/')


def userinfo(request, user_name):
    user = User.objects.get(username=user_name)
    if request.session.get('username'):
        username = request.session["username"]
    else:
        username = ''
    return render(request, 'diaries/userInfo.html', {'user': user, 'username': username})
