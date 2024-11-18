# URL 설정을 위한 Django 기본 모듈 임포트
from django.urls import path, include
from . import views

# URL 네임스페이스 설정
app_name = ""

# URL 패턴 정의
urlpatterns = [
    # 메인 페이지 URL 설정
    # 예: http://localhost:8000/
    path("", views.index, name="index"),
]
