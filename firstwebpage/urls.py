from django.contrib import admin
from django.urls import path
from flatpages import views  #  ИМПОРТИРУЕМ НАШИ VIEWS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  #  ГЛАВНАЯ СТРАНИЦА
    path('hello/', views.hello, name='hello'),  #  СТРАНИЦА /hello/
]