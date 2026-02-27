from functools import cache

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Category, Course
from .serializers import CategorySerializer, CourseSerializer
from .permissions import IsInstructor

# ------------------ Categories ------------------
class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


# ------------------ Public Courses ------------------
class CourseListView(APIView):
    def get(self, request):
        # Data seeded recently; bypassing cache for immediate visibility
        courses = Course.objects.filter(is_published=True)
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


# ------------------ Instructor Courses ------------------
class InstructorCourseCreateView(APIView):
    permission_classes = [IsAuthenticated, IsInstructor]

    def post(self, request):
        data = request.data
        course = Course.objects.create(
            title=data['title'],
            description=data['description'],
            price=data.get('price', 0),
            level=data['level'],
            instructor=request.user,
            category_id=data['category'],
            is_published=False
        )
        return Response({"message": "Course created"})