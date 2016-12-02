from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import AnonymousUser, User
from django.conf import settings
from ..models import TimeStamp
import datetime
from django.utils import timezone

class TimeStampModelTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_secret')

    def testModelInstanceCreation(self):
            ts=TimeStamp(user=self.user,time_stamp=timezone.now())
            self.assertIs(type(ts), TimeStamp)

    def testTimeStampsLimit(self):
        maxStamps=settings.MAX_TIMESTAMPS if settings.MAX_TIMESTAMPS else 5
        for i in range(maxStamps+1):                    #Create more timestamps than the max Value
             self.failUnlessEqual(type(TimeStamp.objects.create_timestamp(self.user)),TimeStamp)
        logintime_list=TimeStamp.objects.filter(user=self.user)
        self.assertIs(len(logintime_list), maxStamps)

    def testLogins(self):
        self.failUnlessEqual(self.client.login(username=self.user.username,password='top_secret'),True)
        self.client.logout()
        logintime_list=TimeStamp.objects.filter(user=self.user)
        self.assertIs( len(logintime_list), 1)

    def testUserDeletion(self):
        self.failUnlessEqual(self.client.login(username=self.user.username,password='top_secret'),True)
        self.client.logout()
        self.user.delete()
        logintime_list=TimeStamp.objects.filter(user=self.user)
        self.assertIs( len(logintime_list), 0)