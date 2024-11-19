from .models import Student4_4
from .serializer import StudentSerializer4_4
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateAPIView , RetrieveDestroyAPIView , RetrieveUpdateDestroyAPIView

# Create your views here.

class StudentListCreateAPI4_4(ListCreateAPIView):
    queryset = Student4_4.objects.all()
    serializer_class = StudentSerializer4_4


class StudentRetrieveUpdateAPI4_4(RetrieveUpdateAPIView):
    queryset = Student4_4.objects.all()
    serializer_class = StudentSerializer4_4


class StudentRetrieveDestroyAPI4_4(RetrieveDestroyAPIView):
    queryset = Student4_4.objects.all()
    serializer_class = StudentSerializer4_4



class StudentRetrieveUpdateDestroyAPI4_4(RetrieveUpdateDestroyAPIView):
    queryset = Student4_4.objects.all()
    serializer_class = StudentSerializer4_4