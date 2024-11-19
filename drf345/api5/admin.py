from django.contrib import admin
from .models import Student5

# Register your models here.

@admin.register(Student5)
class StudentAdmin5(admin.ModelAdmin):
    list_display = ['id' , 'roll' , 'name' , 'city'] 