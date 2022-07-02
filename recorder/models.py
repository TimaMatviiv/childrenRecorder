from django.db import models

# Create your models here.
class Child(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	village = models.CharField(max_length=200)
	ended_class = models.CharField(max_length=200)
	parent_name = models.CharField(max_length=200)
	parent_phone_number = models.CharField(max_length=200)
	health_problems = models.CharField(max_length=1500)
