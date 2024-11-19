from django.contrib import admin
from .models import Student3

# Register your models here.

@admin.register(Student3)
class StudentAdmin3(admin.ModelAdmin):
    list_display = ['id' , 'roll' , 'name' , 'city']