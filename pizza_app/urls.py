from django.contrib import admin
from django.urls import path
from . import views

app_name = "pizza_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('completed_accounts/', views.completed_accounts,
         name='completed_accounts'),
    path('account_details/', views.account_details, name='account_details'),
    path('account_deposit/', views.account_deposit, name='account_deposit'),
    path('account_withdraw/', views.account_withdraw, name='account_withdraw'),
    path('account_transfer/', views.account_transfer, name='account_transfer'),
]
