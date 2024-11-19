from django.contrib import admin
from .models import Student3_3

# Register your models here.

@admin.register(Student3_3)
class StudentAdmin3_3(admin.ModelAdmin):
    list_display = ['id' , 'roll' , 'name' , 'city']