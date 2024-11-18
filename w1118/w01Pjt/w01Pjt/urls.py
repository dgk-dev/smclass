from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("students/", include("students.urls")),  # students 앱의 urls.py 파일을 추가
    path('', include("home.urls")), # home 앱의 urls.py 파일을 추가
    path('board/', include('board.urls')), # board 앱의 urls.py 파일을 추가
]
