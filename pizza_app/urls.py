from django.contrib import admin
from django.urls import path
from . import views

app_name = "pizza_app"

urlpatterns = [
    path('customer_page', views.customer_page, name='customer_page'),
    path('employee_page/', views.employee_page, name='employee_page'),
    path('user_profile/', views.user_profile, name='user_profile'),  # new
    path('base/', views.base, name='base'),
    path('edit_pizza/<int:pizza_id>/', views.edit_pizza, name='edit_pizza'),
    path('delete_pizza/', views.delete_pizza, name='delete_pizza'),
    path('update_pizza/', views.update_pizza, name='update_pizza'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('edit_customers/', views.edit_customers, name='edit_customers'),

]
