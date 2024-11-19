from rest_framework import serializers
from .models import Student4_4

class StudentSerializer4_4(serializers.ModelSerializer):
    class Meta:
        model = Student4_4
        fields = ['id' , 'roll' , 'name' , 'city']