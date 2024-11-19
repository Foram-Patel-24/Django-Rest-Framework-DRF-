from django.shortcuts import render
from rest_framework.response import Response
from .models import Student5
from .serializer import StudentSerializer5
from rest_framework import status
from rest_framework import viewsets

# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self , request) :
        stu = Student5.objects.all()
        serializer = StudentSerializer5(stu , many = True)
        return Response(serializer.data)
    

    def retrieve(self , request , pk = None) :
        id = pk 
        if id is not None :
            stu = Student5.objects.get(id = id)
            serializer = StudentSerializer5(stu)
            return Response(serializer.data)
        

    def create(self , request) :
        serializer = StudentSerializer5(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created.'} , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

    def update(self , request , pk = None) :
        id = pk
        stu = Student5.objects.get(pk = id)
        serializer = StudentSerializer5(stu , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg' : 'Complete Data Updated.'})
        return Response (serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    


    def partial_update(self , request , pk = None):
        id = pk
        stu = Student5.objects.get(pk = id)
        Serializer = StudentSerializer5(stu , data = request.data , partial = True)
        if Serializer.is_valid():
            Serializer.save()
            return Response({'msg' : 'Partial Data Updated.'})
        return Response(Serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

    def delete(self , request , pk = None):
        id =pk
        stu = Student5.objects.get(pk = id)
        stu.delete()
        return Response({'msg' : 'Data Deleted.'})