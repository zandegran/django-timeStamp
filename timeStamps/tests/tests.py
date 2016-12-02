
"""
This is the test module.

This test module has all the test cass for  timeStamps

.. seealso:: :class:`..models.TimeStamp`

"""


from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import AnonymousUser, User
from django.conf import settings
from ..models import TimeStamp
import datetime
from django.utils import timezone

class TimeStampModelTests(TestCase):
	"""
	The container Class that holds all the tests.
	:param TestCase: TestCase module to do test cases.
	
	"""
	def setUp(self):
		"""
        Initial setup for all the test cases.
        A user names jacob is created here and Client is initiated.
        """
		self.client = Client()
        self.user = User.objects.create_user(
   	        username='jacob', email='jacob@gmail.com', password='top_secret')

	def testModelInstanceCreation(self):
		"""
		This test directly tests the model creation.
		Tries to create a timestamp object with curent time and the already created user.

		"""
        ts=TimeStamp(user=self.user,time_stamp=timezone.now())
    	self.assertIs(type(ts), TimeStamp)

	def testTimeStampsLimit(self):
		"""
		This test checks whether the timeStamp didn't exceed the limit.
		This is checked by attempting to create more timestamps than the limit.
		This also checks whether the timeStamp manager is working properly.

    	"""
    	# Tries to get value of MAX_TIMESTAMPS from settings
    	# and if it does not xist assign the value of 5.
    	# This is equivalent of   maxStamps=settings.MAX_TIMESTAMPS if hasattr(settings.MAX_TIMESTAMPS) else 5
        maxStamps=getattr(settings, 'MAX_TIMESTAMPS', 5) 
        for i in range(maxStamps+1):                    # Create more timestamps than the max Value
             self.failUnlessEqual(type(TimeStamp.objects.create_timestamp(self.user)),TimeStamp) # Check whether the timestamps are created successfully.
        logintime_list=TimeStamp.objects.filter(user=self.user)
        self.assertIs(len(logintime_list), maxStamps) # Check whether the timestamp didn't exceed the limit.

	def testLogins(self):
		"""
    	This test checks whether a login action is creating a timeStamp successfully.
    	This also checks whethr a login is successfull.

    	"""
        self.failUnlessEqual(self.client.login(username=self.user.username,password='top_secret'),True) # Checcks whether login is successful.
        self.client.logout()
        logintime_list=TimeStamp.objects.filter(user=self.user)
        self.assertIs( len(logintime_list), 1) # Checks whether a timeeStamp is creatd for the login

	def testUserDeletion(self):
		"""
    	This test checks whether deleting a user also deletes the corresponding timeStamps.
    	This basically checks the integrity of the database.

    	"""
        self.failUnlessEqual(self.client.login(username=self.user.username,password='top_secret'),True)
        self.client.logout()
        self.assertIs( len(logintime_list), 1)
        self.user.delete()
        logintime_list=TimeStamp.objects.filter(user=self.user)
        self.assertIs( len(logintime_list), 0) #  Checks whether a timeeStamp is deleted for the user