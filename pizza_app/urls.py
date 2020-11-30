from django.contrib import admin
from django.urls import path
from . import views

app_name = "pizza_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('employe_page/', views.employe_page, name='employe_page'),
    path('base/', views.base, name='base'),
    path('edit_pizza/', views.edit_pizza, name='edit_pizza'),
]
