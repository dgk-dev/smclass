from django.urls import path, include
from . import views

app_name='home'
urlpatterns = [
    path('', views.index, name="index"), # 메인 페이지는 주로 index 함수로 처리
]
