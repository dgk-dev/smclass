from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "students" # name:url시 사용되는 이름
urlpatterns = [
    path("write/", views.write, name="write1"), # 학생 입력 페이지
    path("list/", views.list, name="list"), # 학생 목록 페이지
]
