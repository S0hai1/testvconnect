# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('our-services/', views.our_services, name='our_services'),
    path('our-services/inbound-call-center-services/', views.inbound_call_center_services, name='inbound_call_center_services'),
    path('our-services/technical-support/', views.technical_support_page, name='technical_support'),
    path('our-services/order-processing-services/', views.order_processing_services, name='order_processing'),
    path('our-services/customer-service-outsourcing/', views.customer_service_outsourcing, name='customer_service_outsourcing'),
    path('our-services/customer-retention-support/', views.customer_retention_support, name='customer_retention_support'),

]
