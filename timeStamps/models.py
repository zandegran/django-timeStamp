from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.conf import settings

from django.contrib.auth.signals import user_logged_in
# Create your models here.

class timeStampManager(models.Manager):
    def create_timestamp(self, user):
        maxStamps=settings.MAX_TIMESTAMPS if settings.MAX_TIMESTAMPS else 5
    	logintime_list=TimeStamp.objects.filter(user=user).order_by('time_stamp')
    	if len(logintime_list) >= maxStamps:
    		for index in range(len(logintime_list)-maxStamps+1):
    			logintime_list[index].delete()
        ts= self.create(time_stamp=timezone.now(),user=user)
        return ts

class TimeStamp(models.Model):
	user=models.ForeignKey(User)
	time_stamp = models.DateTimeField('Logged in')
	objects=timeStampManager()

def addToStorage(sender, user, request, **kwargs):
     TimeStamp.objects.create_timestamp(user)

user_logged_in.connect(addToStorage)