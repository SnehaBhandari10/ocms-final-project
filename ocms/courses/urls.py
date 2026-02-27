from django.urls import path
from .views import (
    CategoryListView,
    CourseListView,
    InstructorCourseCreateView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('courses/', CourseListView.as_view()),
    path('instructor/courses/', InstructorCourseCreateView.as_view()),
]