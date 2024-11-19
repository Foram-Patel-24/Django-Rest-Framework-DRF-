from .models import Student3_3
from .serializer import StudentSerializer3_3
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin , CreateModelMixin , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin

# Create your views here.

class LCStudentAPI3_3(GenericAPIView , ListModelMixin , CreateModelMixin):
    queryset = Student3_3.objects.all()
    serializer_class = StudentSerializer3_3

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class RUDStudentAPI3_3(GenericAPIView , RetrieveModelMixin , UpdateModelMixin , DestroyModelMixin):
    queryset = Student3_3.objects.all()
    serializer_class = StudentSerializer3_3

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)