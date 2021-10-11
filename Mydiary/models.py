from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=40)
	email = models.CharField(max_length=35, unique=True, primary_key=True)
	password = models.CharField(max_length=20)
	



 



class NewEntry(models.Model):
	username = models.CharField(max_length=36,default='admin')
	date = models.DateTimeField(auto_now_add=True)
	Topic = models.CharField(max_length=30,blank=True,null=True ,default='topic')
	TodaysEntry = models.TextField(max_length=1000,blank=False ,default='todaysentry')

class Socials(models.Model):
	bio = models.TextField(max_length=1000,blank=False ,default='hello')
	username = models.CharField(max_length=36,default='admin')
	linkedin = models.URLField(max_length = 200,default='linkedin.com/')
	twitter = models.URLField(max_length = 200,default='twitter.com/')
	facebook = models.URLField(max_length = 200,default='facebook.com/')
	instagram = models.URLField(max_length = 200,default='instagram.com/')
	date = models.DateTimeField(default=datetime.date.today)



	
	 
	  
	  
	  
	  