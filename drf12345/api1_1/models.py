from django.db import models

# Create your models here.


class Student1(models.Model):
     name = models.CharField(max_length=50)
     roll = models.IntegerField()
     city = models.CharField(max_length=50)
