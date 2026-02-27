from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import Enrollment, LectureProgress
from .serializers import (
    EnrollSerializer,
    MyCourseSerializer,
    LectureProgressSerializer
)
from courses.models import Course, Lecture


# ------------------ ENROLL ------------------
# POST /api/enroll/
class EnrollView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EnrollSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course_id = serializer.validated_data['course_id']
        course = Course.objects.get(id=course_id)

        enrollment, created = Enrollment.objects.get_or_create(
            student=request.user,
            course=course
        )

        if not created:
            return Response({"message": "Already enrolled"})

        return Response({"message": "Enrolled successfully"})


# ------------------ MY COURSES ------------------
# GET /api/my-courses/
class MyCoursesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        enrollments = Enrollment.objects.filter(student=request.user)
        serializer = MyCourseSerializer(enrollments, many=True)
        return Response(serializer.data)


# ------------------ COURSE PROGRESS ------------------
# GET /api/course/<id>/progress/
class CourseProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        enrollment = Enrollment.objects.get(
            student=request.user,
            course_id=id
        )

        progress = LectureProgress.objects.filter(enrollment=enrollment)
        serializer = LectureProgressSerializer(progress, many=True)
        return Response(serializer.data)