from .models import Student6_6
from rest_framework import serializers

class StudentSerializer6_6(serializers.ModelSerializer):
    class Meta:
        model = Student6_6
        fields = ['id' , 'roll' , 'name' , 'city']