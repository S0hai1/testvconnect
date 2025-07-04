from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import Admin
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # Potentially use for development, but remove in production
from django.contrib.auth.hashers import check_password # Assuming you're using Django's check_password

# Import your Admin model
from .models import Admin # Adjust this import based on your app structure

def admin_login(request):
    
    admin_id = request.session.get('admin_id')
    if admin_id:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            admin = Admin.objects.get(username=username)
            if check_password(password, admin.password):
                # Login successful
                request.session['admin_id'] = admin.id
                # Return a JSON response for AJAX success
                return JsonResponse({'success': True, 'message': 'Login successful.'})
            else:
                # Invalid password
                return JsonResponse({'success': False, 'message': 'Invalid password.'})
        except Admin.DoesNotExist:
            # Admin not found
            return JsonResponse({'success': False, 'message': 'Admin not found.'})
        except Exception as e:
            # Catch any other unexpected errors
            print(f"Login error: {e}") # Log the error for debugging
            return JsonResponse({'success': False, 'message': 'An unexpected error occurred.'}, status=500)

    # For GET requests or if the POST request didn't result in an AJAX response
    return render(request, 'adminpanel/admin_login.html')

def admin_logout(request):
    request.session.flush()  # Clear all session data
    messages.success(request, 'You have been logged out.')
    return redirect('admin_login')  # Redirect to login page


from django.http import JsonResponse
import random
from .models import Admin

def send_otp_ajax(request):
    if request.method == 'POST':
        identifier = request.POST.get('username')
        if not identifier:
            return JsonResponse({'success': False, 'message': 'Username or email is required.'})

        try:
            admin = Admin.objects.get(username=identifier)
        except Admin.DoesNotExist:
            try:
                admin = Admin.objects.get(email=identifier)
            except Admin.DoesNotExist:
                return JsonResponse({'success': False, 'message': 'Admin not found.'})

        otp = str(random.randint(100000, 999999))
        request.session['reset_otp'] = otp
        request.session['reset_admin_id'] = admin.id

        print(f"[DEBUG] OTP for {admin.username}: {otp}")  # or send via email in real app

        return JsonResponse({'success': True, 'message': 'OTP sent.', 'otp': otp})  # send `otp` only in demo mode
    return JsonResponse({'success': False, 'message': 'Invalid request.'})


def verify_otp_ajax(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        session_otp = request.session.get('reset_otp')

        if entered_otp == session_otp:
            return JsonResponse({'success': True, 'message': 'OTP verified.'})
        return JsonResponse({'success': False, 'message': 'Invalid OTP.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request.'})


from django.contrib.auth.hashers import make_password

def reset_password_ajax(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password != confirm_password:
            return JsonResponse({'success': False, 'message': 'Passwords do not match.'})

        admin_id = request.session.get('reset_admin_id')
        if not admin_id:
            return JsonResponse({'success': False, 'message': 'Session expired.'})

        try:
            admin = Admin.objects.get(id=admin_id)
            admin.password = make_password(new_password)
            admin.save()

            request.session.flush()  # clear session after reset
            return JsonResponse({'success': True, 'message': 'Password updated.'})
        except Admin.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Admin not found.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request.'})

def admin_dashboard(request):
    if 'admin_id' not in request.session:
        messages.error(request, 'You need to log in first.')
        return redirect('admin_login')

    # Fetch admin details for the dashboard
    admin = Admin.objects.get(id=request.session['admin_id'])
    return render(request, 'adminpanel/dashboard.html', {'admin': admin})