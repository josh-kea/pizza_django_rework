from django.contrib import admin
from django.urls import path
from . import views

app_name = "pizza_app"

urlpatterns = [
    path('', views.customer_page, name='customer_page'),
    path('employee_page/', views.employee_page, name='employee_page'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('base/', views.base, name='base'),
    path('edit_pizza/', views.edit_pizza, name='edit_pizza'),
    
]
