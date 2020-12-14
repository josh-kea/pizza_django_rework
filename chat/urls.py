# chat/urls.py
from django.urls import path

from . import views
from login_app import urls as login_apps

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]