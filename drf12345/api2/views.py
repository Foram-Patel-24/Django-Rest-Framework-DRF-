from django.shortcuts import render
from rest_framework.response import Response
from .models import Student2
from .serializer import StudentSerializer2
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


class StudentAPI2(APIView):
    def get(self , request , pk = None , format=None):
        id = pk
        if id is not None:
            stu = Student2.objects.get(id = id)
            serializer = StudentSerializer2(stu)
            return Response(serializer.data)
        
        stu = Student2.objects.all()
        serializer = StudentSerializer2(stu , many = True)
        return Response(serializer.data)
    



    def display(self , request , format = None):
        serializer = StudentSerializer2(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created.'} , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    


    def put(self , request , pk, format = None):
        id = pk
        stu = Student2.objects.get(pk = id)
        serializer = StudentSerializer2(stu , request.data)
        if serializer.is_valid():
                serializer.save()
                return Response({'msg' : 'Complete Data Updated.'})
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    


    def patch(self , request , pk, format = None):
         id = pk
         stu = Student2.objects.get(pk = id)
         Serializer = StudentSerializer2(stu , request.data , partial = True)
         if Serializer.is_valid():
              Serializer.save()
              return Response({'msg' : 'Partial Data Updated.'})
         return Response(Serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    


    def delete(self , request , pk, foramt = None):
         id = pk 
         stu = Student2.objects.get(pk = id)
         stu.delete()
         return Response({'msg' : 'Data Deleted.'})