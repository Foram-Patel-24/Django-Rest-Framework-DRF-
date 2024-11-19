from rest_framework import serializers
from .models import Student3_3

class StudentSerializer3_3(serializers.ModelSerializer):
    class Meta:
        model = Student3_3
        fields = ['id' , 'roll' , 'name' , 'city']