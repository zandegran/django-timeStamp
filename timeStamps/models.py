"""
This is where the models are defined.

"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from django.conf import settings

from django.contrib.auth.signals import user_logged_in


class timeStampManager(models.Manager):
    def create_timestamp(self, user):
        """
        Creates TimeStamp for a user
        :param self instance of the timeStampManager object.
        :param user User for which the TimeStamp is createed.
        :return retuurns the createed TimeStamp.

        """
        # Tries to get value of MAX_TIMESTAMPS from settings
        # and if it does not xist assign the value of 5
        # This is equivalent of   maxStamps=settings.MAX_TIMESTAMPS if hasattr(settings.MAX_TIMESTAMPS) else 5
        maxStamps=getattr(settings, 'MAX_TIMESTAMPS', 5)
        logintime_list=TimeStamp.objects.filter(user=user).order_by('time_stamp')
        if len(logintime_list) >= maxStamps:
            for index in range(len(logintime_list)-maxStamps+1): # Delete on more than the max timeStamps allowed. This also creates room for the new one  
                logintime_list[index].delete()
        ts= self.create(time_stamp=timezone.now(),user=user)  # Create a new entry
        return ts


# The only model used is here.
class TimeStamp(models.Model):
	user=models.ForeignKey(User)
	time_stamp = models.DateTimeField('Logged in')
	objects=timeStampManager()  # Object used for creation

def addToStorage(sender, user, request, **kwargs):
     TimeStamp.objects.create_timestamp(user)  # Adds the timestamp in the database

user_logged_in.connect(addToStorage) # Called when ever a user logs in 