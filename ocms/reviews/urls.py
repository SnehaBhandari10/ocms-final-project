from django.urls import path
from .views import AddReviewView, CourseReviewListView

urlpatterns = [
    path('reviews/add/', AddReviewView.as_view()),
    path('course/<int:id>/reviews/', CourseReviewListView.as_view()),
]