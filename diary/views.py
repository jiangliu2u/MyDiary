from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic
from .models import Diary
from django.utils import timezone
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
        username = request.POST.get('name', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            request.session['username'] = username
            print('登录成功')
            return HttpResponseRedirect('/diary/')
        else:
            print("用户名或密码错误")
            return HttpResponseRedirect('/diary/logina')



def index(request):#首页
    all_diaries = Diary.objects.order_by('-pub_date')
    if request.session.get('username'):
        username = request.session["username"]
    else:
        username = ''
    return render_to_response('diaries/index.html', {'username': username, 'all_diaries': all_diaries})


def logout(request):#注销
    del request.session["username"]
    return HttpResponseRedirect('/diary/')


def userinfo(request, user_name):#用户详情
    user = User.objects.get(username=user_name)
    if request.session.get('username'):
        username = request.session["username"]
    else:
        username = ''
    return render(request, 'diaries/userInfo.html', {'user': user, 'username': username})

def postDiary(request):#写日记
    if request.method == 'POST':
        username = request.session["username"]
        user = User.objects.get(username = username)
        content = request.POST.get("diary_content",'')
        mood = request.POST.get("mood",'')
        pub_date = timezone.now()
        diary = Diary(user = user, content = content, mood = mood, pub_date=pub_date)
        diary.save()
        return HttpResponseRedirect('/diary/')





def postPage(request):#写日记页面
    if request.session.get('username'):
        username = request.session["username"]
    else:
        username=''
    return render(request, 'diaries/postDiary.html',{"username":username})

        
def regPage(request):    #注册页面
    if request.session.get('username'):
        username = request.session["username"]
    else:
        username=''
    return render(request, 'diaries/regPage.html',{"username":username})


# def register(request):#用户注册
#     if request.method='POST':
#         usern