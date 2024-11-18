from django.urls import path, include
from . import views

app_name = 'index'       ## name : url 연결시 사용
urlpatterns = [
    path('', views.index, name='index'), # 메인페이지 : index, main, default로 주로 사용함.
]
