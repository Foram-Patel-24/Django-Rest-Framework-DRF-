# GenericAPIView & Model Mixin

from .models import Student
from.serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin



# List And Create - PK not Required

class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self , request , *args , **kwargs):
        return self.list(request , *args , **kwargs)
    
    def post(self , request , *args , **kwargs):
        return self.create(request , *args , **kwargs)
    

# Retrieve , Update & Destroy - PK is Required

class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self , request , *args , **kwargs):
        return self.retrieve(request , *args , **kwargs)
    
    def put(self , request , *args , **kwargs):
        return self.update(request , *args , **kwargs)
    
    def delete(self , request , *args , **kwargs):
        return self.delete(request , *args , **kwargs)
   
