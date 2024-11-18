from django.urls import path, include
from . import views

app_name = 'students'       ## name : url 연결시 사용
urlpatterns = [
    path('write/', views.write, name='write'), # 학생입력페이지
    path('dowrite/', views.dowrite, name='dowrite'), # 학생입력페이지
]
