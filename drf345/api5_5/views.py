from django.shortcuts import render
from rest_framework.response import Response
from .models import Student5_5
from .serializer import StudentSerializer5_5
from rest_framework import status , viewsets

# Create your views here.


class StudentViewSet5(viewsets.ViewSet):
    def list(self , request):
        print("******** List ********")
        print("BaseName : " , self.basename)
        print("Action   : " , self.action)
        print("Details  : " , self.detail)
        print("Suffix   : " , self.suffix)
        print("Name     : " , self.name)
        print("Description : " , self.description)

        stu = Student5_5.objects.all()
        serializer = StudentSerializer5_5(stu , many = True)
        return Response(serializer.data)
    


    def retrieve(self , request , pk = None):
        print("******** Retrieve ********")
        print("BaseName : " , self.basename)
        print("Action   : " , self.action)
        print("Details  : " , self.detail)
        print("Suffix   : " , self.suffix)
        print("Name     : " , self.name)
        print("Description : " , self.description)

        id = pk
        if id is not None :
            stu = Student5_5.objects.get(id = id)
            serializer = StudentSerializer5_5(stu)
            return Response(serializer.data)
        



    def create(self , request):
        print("******** Create ********")
        print("BaseName : " , self.basename)
        print("Action   : " , self.action)
        print("Details  : " , self.detail)
        print("Suffix   : " , self.suffix)
        print("Name     : " , self.name)
        print("Description : " , self.description)

        serializer = StudentSerializer5_5(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data Created.'} , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)



    def update(self , request ,pk = None):
        print("******** Update ********")
        print("BaseName : " , self.basename)
        print("Action   : " , self.action)
        print("Details  : " , self.detail)
        print("Suffix   : " , self.suffix)
        print("Name     : " , self.name)
        print("Description : " , self.description)

        id = pk
        stu = Student5_5.objects.get(id = id)  
        serializer = StudentSerializer5_5(stu , data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Complete Data Updated.'})
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST) 
    


    def partial_update(self , request , pk = None):
        print("******** Partial Update ********")
        print("BaseName : " , self.basename)
        print("Action   : " , self.action)
        print("Details  : " , self.detail)
        print("Suffix   : " , self.suffix)
        print("Name     : " , self.name)
        print("Description : " , self.description)

        id = pk
        stu = Student5_5.objects.get(id = id)
        serializer = StudentSerializer5_5(stu , data = request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data Updated.'})
        return Response (serializer.errors , status = status.HTTP_400_BAD_REQUEST)


    def destroy(self , request , pk = None):
        print("******** Delete ********")
        print("BaseName : " , self.basename)
        print("Action   : " , self.action)
        print("Details  : " , self.detail)
        print("Suffix   : " , self.suffix)
        print("Name     : " , self.name)
        print("Description : " , self.description)

        id = pk
        stu = Student5_5.objects.get(pk = id)
        stu.delete()
        return Response({'msg' : 'Data Deleted.'})