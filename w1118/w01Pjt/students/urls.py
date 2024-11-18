from django.urls import path, include
from . import views

app_name = 'students'       ## name : url 연결시 사용
urlpatterns = [
    path('list/', views.list, name='list'), # 학생리스트
    path('write/', views.write, name='write'), # 학생입력페이지
    path('<str:name>/view/', views.view, name='view' ), # 학생상세페이지 만약 정수를 받는 것이면 <int:no>

    path('<str:name>/modify/', views.modify, name='modify' ), # 학생수정페이지
    path('modify2/', views.modify2, name='modify2' ), # 학생수정페이지 - GET 파라미터
    path('<str:name>/modify3/', views.modify3, name='modify3' ), # 학생수정페이지
    path('<str:name>/delte/', views.delete, name='delete' ), # 학생수정페이지

    # path('dowrite/', views.dowrite, name='dowrite'), # 학생입력페이지
]
