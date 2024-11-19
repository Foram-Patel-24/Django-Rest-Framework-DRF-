from django.shortcuts import render
from .models import Student6
from .serializer import StudentSerializer6
from rest_framework import viewsets

# Create your views here.


class StudentModelViewSet6(viewsets.ModelViewSet):
    queryset = Student6.objects.all()
    serializer_class = StudentSerializer6


    ''' def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)  '''