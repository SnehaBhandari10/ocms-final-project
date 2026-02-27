from rest_framework import serializers
from .models import Enrollment, LectureProgress


class EnrollSerializer(serializers.Serializer):
    course_id = serializers.IntegerField()


class MyCourseSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(
        source='course.title',
        read_only=True
    )

    class Meta:
        model = Enrollment
        fields = ['id', 'course_title', 'status', 'enrolled_at']


class LectureProgressSerializer(serializers.ModelSerializer):
    lecture_title = serializers.CharField(
        source='lecture.title',
        read_only=True
    )

    class Meta:
        model = LectureProgress
        fields = ['lecture_title', 'completed', 'completed_at']