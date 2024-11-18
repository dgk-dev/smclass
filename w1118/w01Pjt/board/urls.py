from django.urls import path, include
from . import views

app_name = 'board'       ## name : url 연결시 사용
urlpatterns = [
    path('list/', views.list, name='list'), # 메인페이지 : index, main, default로 주로 사용함.
]
