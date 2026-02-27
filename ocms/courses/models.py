from django.db import models
from accounts.models import User
from django.db.models import Avg

# ------------------ Category ------------------
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ------------------ Course ------------------
class Course(models.Model):
    LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)

    instructor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'INSTRUCTOR'}
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def average_rating(self):
        return self.reviews.aggregate(avg=Avg('rating'))['avg']
    


# ------------------ Module ------------------
class Module(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='modules'
    )
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ('course', 'order')

    def __str__(self):
        return f"{self.course.title} - {self.title}"


# ------------------ Lecture ------------------
class Lecture(models.Model):
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name='lectures'
    )
    title = models.CharField(max_length=255)
    video_url = models.TextField()
    notes = models.TextField(blank=True)
    order = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duration in seconds")

    class Meta:
        unique_together = ('module', 'order')

    def __str__(self):
        return self.title