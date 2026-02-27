from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    student_email = serializers.CharField(
        source='student.email',
        read_only=True
    )

    class Meta:
        model = Review
        fields = [
            'id',
            'student_email',
            'rating',
            'comment',
            'created_at'
        ]


class AddReviewSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField(required=False, allow_blank=True)