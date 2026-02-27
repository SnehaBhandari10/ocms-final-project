import os
import django
import random

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ocms.settings')
django.setup()

from accounts.models import User
from courses.models import Category, Course, Module, Lecture

def seed():
    print("Starting data seeding...")

    # 1. Create Categories
    categories_data = [
        {"name": "Computer Science", "slug": "cs"},
        {"name": "Business & Management", "slug": "business"},
        {"name": "Humanities & Arts", "slug": "humanities"},
        {"name": "Science & Engineering", "slug": "engineering"},
        {"name": "Education & Pedagogy", "slug": "education"},
    ]
    
    cats = []
    for data in categories_data:
        cat, _ = Category.objects.get_or_create(name=data['name'], slug=data['slug'])
        cats.append(cat)
    print(f"Created {len(cats)} categories.")

    # 2. Create Instructors
    instructors_data = [
        {"email": "prof.smith@university.edu", "full_name": "Prof. Alan Smith", "role": "INSTRUCTOR"},
        {"email": "dr.sarah@academy.com", "full_name": "Dr. Sarah Jenkins", "role": "INSTRUCTOR"},
        {"email": "instructor.lee@ocms.com", "full_name": "Marcus Lee", "role": "INSTRUCTOR"},
    ]
    
    instructors = []
    for data in instructors_data:
        user, created = User.objects.get_or_create(email=data['email'], defaults={
            "full_name": data['full_name'],
            "role": data['role']
        })
        if created:
            user.set_password("pass123")
            user.save()
        instructors.append(user)
    print(f"Created {len(instructors)} instructors.")

    # 3. Create Courses
    courses_data = [
        # CS Degree
        {
            "title": "Full-Stack Web Development with Django", 
            "description": "Learn to build professional SaaS applications from scratch.",
            "price": 4999.00, "level": "Intermediate", "cat": cats[0], "inst": instructors[0]
        },
        {
            "title": "Data Structures & Algorithms", 
            "description": "Master the fundamentals of efficient coding and system design.",
            "price": 2999.00, "level": "Advanced", "cat": cats[0], "inst": instructors[0]
        },
        # Business Degree
        {
            "title": "Strategic Leadership in the Digital Age", 
            "description": "Scale teams and lead organizations through digital transformation.",
            "price": 8900.00, "level": "Advanced", "cat": cats[1], "inst": instructors[1]
        },
        {
            "title": "Financial Literacy for Entrepreneurs", 
            "description": "Understand cashflow, equity, and scaling your business.",
            "price": 1200.00, "level": "Beginner", "cat": cats[1], "inst": instructors[1]
        },
        # Education Degree (for teachers)
        {
            "title": "Advanced Instructional Design", 
            "description": "Courses designed for educators to master the art of curriculum building.",
            "price": 5500.00, "level": "Advanced", "cat": cats[4], "inst": instructors[2]
        },
        {
            "title": "Classroom Psychology & Management", 
            "description": "Techniques for fostering engaging and inclusive learning environments.",
            "price": 1500.00, "level": "Intermediate", "cat": cats[4], "inst": instructors[2]
        }
    ]

    for data in courses_data:
        course, _ = Course.objects.get_or_create(
            title=data['title'],
            defaults={
                "description": data['description'],
                "price": data['price'],
                "level": data['level'],
                "category": data['cat'],
                "instructor": data['inst'],
                "is_published": True
            }
        )
        
        # Add a couple of modules
        for i in range(1, 4):
            mod, _ = Module.objects.get_or_create(
                course=course, order=i,
                defaults={"title": f"Module {i}: Fundamental Concepts"}
            )
            # Add a couple of lectures
            for j in range(1, 3):
                Lecture.objects.get_or_create(
                    module=mod, order=j,
                    defaults={
                        "title": f"Lecture {j}: Introduction to Logic",
                        "video_url": "https://example.com/video",
                        "duration": 600,
                        "notes": "Key takeaways for this session."
                    }
                )

    print("Seeding completed successfully!")

if __name__ == "__main__":
    seed()
