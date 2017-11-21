from django.shortcuts import render
from django.views import generic
from .models import Diary


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
