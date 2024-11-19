from .models import Student3
from .serializer import StudentSerializer3
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin 

# Create your views here.

class StudentList(GenericAPIView , ListModelMixin):
    queryset = Student3.objects.all()
    serializer_class = StudentSerializer3

    def get(self , request , *args , **kwargs):
        return self.list(request , *args , **kwargs)
    


class StudentCreate(GenericAPIView , CreateModelMixin):
    queryset = Student3.objects.all()
    serializer_class = StudentSerializer3

    def post(self , request , *args , **kwargs):
        return self.create(request , *args , **kwargs)
    

class StudentRetrieve(GenericAPIView , RetrieveModelMixin):
    queryset = Student3.objects.all()
    serializer_class = StudentSerializer3

    def get(self , request , *args , **kwargs):
        return self.retrieve(request , *args , **kwargs)
    


class StudentUpdate(GenericAPIView , UpdateModelMixin):
    queryset = Student3.objects.all()
    serializer_class = StudentSerializer3

    def put(self , request , *args , **kwargs):
        return self.update(request , *args , **kwargs)
    


class StudentDestroy(GenericAPIView , DestroyModelMixin):
    queryset = Student3.objects.all()
    serializer_class = StudentSerializer3

    def delete(self , request , *args , **kwargs):
        return self.destroy(request , *args , **kwargs)
    