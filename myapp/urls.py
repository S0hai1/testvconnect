# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('our-services/', views.our_services, name='our_services'),
    path('our-services/inbound-call-center-services/', views.inbound_call_center_services, name='inbound_call_center_services'),
    path('our-services/customer-service/', views.customer_service_page, name='customer_service'),
    path('our-services/technical-support/', views.technical_support_page, name='technical_support'),
]
