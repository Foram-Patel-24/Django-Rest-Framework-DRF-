from django.contrib import admin
from .models import Student6

# Register your models here.


@admin.register(Student6)
class StudentAdmin6(admin.ModelAdmin):
    list_display = ['id' , 'roll' , 'name' , 'city']