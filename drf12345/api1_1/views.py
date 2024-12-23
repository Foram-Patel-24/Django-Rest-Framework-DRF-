from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student1
from .serializer import StudentSerializer1
from rest_framework import status

# Create your views here.

@api_view(['GET' , 'POST' , 'PUT' , 'PATCH' , 'DELETE'])

def student_api1(request , pk = None):
    if request.method == 'GET':
        id = pk
        if id is not None :
            stu = Student1.objects.get(id = id)
            serializer = StudentSerializer1(stu)
            return Response(serializer.data)
        stu = Student1.objects.all()
        serializer = StudentSerializer1(stu , many = True)
        return Response(serializer.data)
    

    if request.method == 'POST' : 
        serializer = StudentSerializer1(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created.'} , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PUT':
        id = pk
        stu = Student1.objects.get(pk = id)
        serializer = StudentSerializer1(stu , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Complete Data Updated.'})
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PATCH':
        id = pk
        stu = Student1.objects.get(pk = id)
        serializer = StudentSerializer1(stu , data = request.data , partial = True )
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data Updated.'})
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        id = pk
        stu = Student1.objects.get(pk = id)
        stu.delete()
        return Response({'msg' : 'Data Deleted.'})
    