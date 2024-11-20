from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member/', include('member.urls')),
    path('product/', views.product_form, name='product_form'),
    path('', include('home.urls')),
]
