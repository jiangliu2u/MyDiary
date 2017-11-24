from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'diary'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^logina/', views.logina, name='logina'),
	url(r'^login/',views.login,name='login'),
	#url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]
