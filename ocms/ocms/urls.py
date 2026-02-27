from django.contrib import admin
from django.urls import path, include
from dashboard import views as dashboard_views
from django.shortcuts import render

def home_view(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Frontend Pages
    path('', dashboard_views.home, name='home'),
    path('login/', dashboard_views.login_page, name='login'),
    path('register/', dashboard_views.register_page, name='register'),
    path('courses-page/', dashboard_views.courses_page, name='courses_page'),
    path('student-dashboard/', dashboard_views.student_dashboard, name='student_dashboard'),
    path('instructor-dashboard/', dashboard_views.instructor_dashboard, name='instructor_dashboard'),
    path('admin-dashboard/', dashboard_views.admin_dashboard, name='admin_dashboard'),

    # API URLs
    path('api/accounts/', include('accounts.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/enrollments/', include('enrollments.urls')),
    path('api/reviews/', include('reviews.urls')),
]




