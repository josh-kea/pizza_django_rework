from django.urls import path
from . import views


app_name = 'login_app'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset_secret/<str:secret>/',
         views.password_reset_secret, name='password_reset_secret'),
    path('password_reset_form/', views.password_reset_form,
         name='password_reset_form'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
