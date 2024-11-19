from django.contrib import admin
from .models import Student6_6

# Register your models here.

@admin.register(Student6_6)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'roll' , 'name' , 'city']