from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

# custom User Manager (using email as login) ------------------
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, role='STUDENT'):
        if not email:
            raise ValueError("Email is required")

        user = self.model(
            email=self.normalize_email(email),
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
            role='ADMIN'
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# Custom User Model ------------------
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('STUDENT', 'Student'),
        ('INSTRUCTOR', 'Instructor'),
        ('ADMIN', 'Admin'),
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()   # ✅ VERY IMPORTANT

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []      # ✅ REQUIRED BY DJANGO

    def __str__(self):
        return self.email