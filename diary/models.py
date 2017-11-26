from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Diary(models.Model):
    user = models.ForeignKey(User, default='')
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date_published')
    mood = models.CharField(max_length=10)
