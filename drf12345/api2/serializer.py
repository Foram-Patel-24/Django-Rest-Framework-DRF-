from rest_framework import serializers
from .models import Student2

class StudentSerializer2(serializers.ModelSerializer):
    class Meta :
        model = Student2
        fields = ['id' , 'roll' , 'name' , 'city']