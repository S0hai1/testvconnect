from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def our_services(request):
    return render(request, 'myapp/our_services.html')

def inbound_call_center_services(request):
    return render(request, 'myapp/inbound_call_center_services.html')

def technical_support_page(request):
    return render(request, 'myapp/technical_support_page.html')

def order_processing_services(request):
    return render(request, 'myapp/order_processing_services.html')

def customer_service_outsourcing(request):
    return render(request, 'myapp/customer_service_outsourcing.html')

def customer_retention_support(request):
    return render(request, 'myapp/customer_retention_support.html')