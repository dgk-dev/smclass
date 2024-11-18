from django.contrib import admin
from students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['s_name', 's_major', 's_age']

# admin 페이지에 Student 모델 등록
admin.site.register(Student)

