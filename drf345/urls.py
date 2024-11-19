"""
URL configuration for drf345 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from api3_3 import views
from api4 import views
from api4_4 import views
from api5 import views
from api5_5 import views
from api6 import views
from api6_6 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register('studentapiview' , views.StudentViewSet , basename = 'student')
# router.register('studentapiview' , views.StudentViewSet5 , basename = 'student')
# router.register('studentapiview' , views.StudentModelViewSet6 , basename = 'student')
router.register('studentapiview' , views.StudentModelViewSetReadOnly , basename = 'student')

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('studentapilc3/' , views.LCStudentAPI3_3.as_view()),
   # path('studentapirud3/<int:pk>' , views.RUDStudentAPI3_3.as_view()),
   # path('studentlist4/' , views.StudentListAPI4.as_view()) ,
   # path('studentcreate4/' , views.StudentCreateAPI4.as_view()) ,
   # path('studentretrieve4/<int:pk>' , views.studentRetrieveAPI4.as_view()) ,
   # path('studentupdate4/<int:pk>' , views.StudentUpdateAPI4.as_view()) ,
   # path('studentdestroy4/<int:pk>' , views.StudentDestroyAPI4.as_view()) ,
   # path('lcstudapi4/' , views.StudentListCreateAPI4_4.as_view()) ,
   # path('rustudapi4/<int:pk>' , views.StudentRetrieveUpdateAPI4_4.as_view()) , 
   # path('rdstudapi4/<int:pk>' , views.StudentRetrieveDestroyAPI4_4.as_view()) ,
   # path('rudstudapi4/<int:pk>' , views.StudentRetrieveUpdateDestroyAPI4_4.as_view()),

   path('' , include(router.urls)),
]
