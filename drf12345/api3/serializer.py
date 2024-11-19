from rest_framework import serializers
from .models import Student3

class StudentSerializer3(serializers.ModelSerializer):
    class Meta :
          model = Student3
          fields = ['id' , 'roll' , 'name' , 'city']