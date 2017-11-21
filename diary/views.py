from django.shortcuts import render
from django.views import generic
from .models import Diary


class IndexView(generic.ListView):
    template_name = 'diaries/index.html'
    context_object_name = 'latest_question_list'


class DetailView(generic.DetailView):
    model = Diary
    template_name = 'diaries/detail.html'
