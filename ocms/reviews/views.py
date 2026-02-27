from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer, AddReviewSerializer
from courses.models import Course
from enrollments.models import Enrollment


# ------------------ ADD REVIEW ------------------
# POST /api/reviews/add/
class AddReviewView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course_id = serializer.validated_data['course_id']
        rating = serializer.validated_data['rating']
        comment = serializer.validated_data.get('comment', '')

        course = Course.objects.get(id=course_id)

        # ensure student is enrolled
        if not Enrollment.objects.filter(
            student=request.user,
            course=course
        ).exists():
            return Response(
                {"error": "You must be enrolled to review this course"},
                status=400
            )

        review, created = Review.objects.get_or_create(
            student=request.user,
            course=course,
            defaults={
                'rating': rating,
                'comment': comment
            }
        )

        if not created:
            return Response(
                {"error": "You have already reviewed this course"},
                status=400
            )

        return Response({"message": "Review added successfully"})


# ------------------ COURSE REVIEWS ------------------
# GET /api/course/<id>/reviews/
class CourseReviewListView(APIView):
    def get(self, request, id):
        reviews = Review.objects.filter(course_id=id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)