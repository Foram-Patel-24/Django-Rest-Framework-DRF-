from django.contrib import admin
from .models import Student2

# Register your models here.

@admin.register(Student2)
class StudentAdmin2(admin.ModelAdmin):
    list_display = ['id' , 'roll' , 'name' , 'city']