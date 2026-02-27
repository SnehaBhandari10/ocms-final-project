from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enrollments.models import Enrollment

@login_required
def dashboard_view(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    return render(request, 'dashboard.html', {
        'enrollments': enrollments
    })


from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

def courses_page(request):
    return render(request, 'courses.html')

def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def instructor_dashboard(request):
    return render(request, 'instructor_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')