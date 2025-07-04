# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('logout/', views.admin_logout, name='admin_logout'),
    path('ajax/send-otp/', views.send_otp_ajax, name='send_otp_ajax'),
    path('ajax/verify-otp/', views.verify_otp_ajax, name='verify_otp_ajax'),
    path('ajax/reset-password/', views.reset_password_ajax, name='reset_password_ajax'),
    
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
