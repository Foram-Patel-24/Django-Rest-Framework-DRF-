from rest_framework import serializers
from .models import Student

# Validators

def start_with_r(value):
    if value[0].lower() != 'r' :
        raise serializers.ValidationError('Name should be start with R')


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = ['name' , 'roll' , 'city']
   
    
# FIELD LEVEL VALIDATION 

    def validate_roll(self , value):
        if value >= 200 :
            raise serializers.ValidationError('Seat Full')
        return value 


# OBJECT LEVEL VALIDATION

    def validate(self , data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'dfd' and ct.lower() != 'jnd' :
            raise serializers.ValidationError('City must be JND')
        return data
    
