from django.db import models
from accounts.models import User
from courses.models import Course, Lecture

# ------------------ Enrollment ------------------
class Enrollment(models.Model):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'STUDENT'}
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.email} - {self.course.title}"


# ------------------ Lecture Progress ------------------
class LectureProgress(models.Model):
    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name='progress'
    )
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('enrollment', 'lecture')

    def __str__(self):
        return f"{self.lecture.title} - {self.completed}"