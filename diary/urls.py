from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'diary'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^logina/', views.logina, name='logina'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]
