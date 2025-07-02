from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def our_services(request):
    return render(request, 'myapp/our_services.html')

def inbound_call_center_services(request):
    return render(request, 'myapp/inbound_call_center_services.html')

def customer_service_page(request):
    return render(request, 'myapp/customer_service_page.html')

def technical_support_page(request):
    return render(request, 'myapp/technical_support_page.html')