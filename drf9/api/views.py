from django.shortcuts import render 
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET" :
        return Response({'msg' : 'This is GET Request'})
    
    if request.method == "POST":
        print(request.data)
        return Response({'msg' : 'This is POST Request' , 'data' : request.data})
    