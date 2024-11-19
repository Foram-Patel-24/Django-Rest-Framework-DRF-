from django.contrib import admin
from .models import Student4_4

# Register your models here.

@admin.register(Student4_4)
class StudentAdmin4_4(admin.ModelAdmin):
    list_display = ['id' , 'roll' , 'name' , 'city']