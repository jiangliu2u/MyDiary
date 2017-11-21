from django.db import models
from django.utils import timezone


# Create your models here.

class Diary(models.Model):
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date_published')
    mood = models.CharField(max_length=10)
