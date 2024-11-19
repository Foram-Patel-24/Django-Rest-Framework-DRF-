from .models import Student4
from rest_framework import serializers

class StudentSerializer4(serializers.ModelSerializer):
    class Meta :
        model = Student4
        fields = ['id' , 'roll' , 'name' , 'city']