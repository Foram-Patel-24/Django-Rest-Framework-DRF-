from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 
# from api.customauth import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
   # authentication_classes = [CustomAuthentication]    
   # authentication_classes = [JWTAuthentication]    
   # permission_classes = [IsAuthenticated]    
 