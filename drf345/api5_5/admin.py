from django.contrib import admin
from .models import Student5_5

# Register your models here.

@admin.register(Student5_5)
class StudentSerializer5_5(admin.ModelAdmin):
    list_display = ['id' , 'roll' , 'name' , 'city'] 