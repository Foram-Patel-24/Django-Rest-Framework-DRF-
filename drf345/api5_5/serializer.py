from rest_framework import serializers
from .models import Student5_5

class StudentSerializer5_5(serializers.ModelSerializer):
    class Meta :
        model = Student5_5
        fields = ['id' , 'roll' , 'name' , 'city']