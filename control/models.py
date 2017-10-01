from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class mailbox(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	message = models.TextField()
	date = models.DateField(default=datetime.today())
	Read = 'Read'
	Unread = 'Unread'
	classification_choices = {
	(Read, 'Read'),
	(Unread, 'Unread'),
	}
	classifications = models.CharField(max_length=200, choices=classification_choices, default="Unread")

	def __str__(self):
	    return str(self.name) +"," + " " + str(self.classifications)



class order(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	tel = models.CharField(max_length=15)
	date = models.DateField(default=datetime.today())
	address = models.CharField(max_length=200)
	category = models.CharField(max_length=500)
	description = models.TextField()
	classification = models.CharField(max_length=50, default="Unread")
	mailed = models.CharField(max_length=1, default='N')


	def __str__(self):
	    return str(self.name) +"," + " " + str(self.category)



