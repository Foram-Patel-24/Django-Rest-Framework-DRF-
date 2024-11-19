from django.contrib import admin
from .models import Student4

# Register your models here.

@admin.register(Student4)
class StudentAdmin4(admin.ModelAdmin):
    list_display = ['id' , 'roll' , 'name' ,'city']