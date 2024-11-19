from django.shortcuts import render
from .models import Student6_6
from .serializer import StudentSerializer6_6
from rest_framework import viewsets

# Create your views here.


class StudentModelViewSetReadOnly(viewsets.ReadOnlyModelViewSet):
    queryset = Student6_6.objects.all()
    serializer_class = StudentSerializer6_6