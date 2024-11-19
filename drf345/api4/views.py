from .serializer import StudentSerializer4
from .models import Student4
from rest_framework.generics import ListAPIView , CreateAPIView , RetrieveAPIView , UpdateAPIView , DestroyAPIView

# Create your views here.

class StudentListAPI4(ListAPIView):
    queryset = Student4.objects.all()
    serializer_class = StudentSerializer4


class StudentCreateAPI4(CreateAPIView):
    queryset = Student4.objects.all()
    serializer_class = StudentSerializer4


class studentRetrieveAPI4(RetrieveAPIView):
    queryset = Student4.objects.all()
    serializer_class = StudentSerializer4


class StudentUpdateAPI4(UpdateAPIView):
    queryset = Student4.objects.all()
    serializer_class = StudentSerializer4


class StudentDestroyAPI4(DestroyAPIView):
    queryset = Student4.objects.all()
    serializer_class = StudentSerializer4