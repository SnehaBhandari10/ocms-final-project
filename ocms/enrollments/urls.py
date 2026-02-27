from django.urls import path
from .views import EnrollView, MyCoursesView, CourseProgressView

urlpatterns = [
    path('enroll/', EnrollView.as_view()),
    path('my-courses/', MyCoursesView.as_view()),
    path('course/<int:id>/progress/', CourseProgressView.as_view()),
]