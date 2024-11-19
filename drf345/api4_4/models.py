from django.db import models

# Create your models here.

class Student4_4(models.Model):
    name = models.CharField(max_length=58)
    roll = models.IntegerField()
    city = models.CharField(max_length=58)