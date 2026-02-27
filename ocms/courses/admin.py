from django.contrib import admin
from .models import Category, Course, Module, Lecture


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "created_at")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "level", "price", "is_published")
    list_filter = ("level", "is_published")
    search_fields = ("title",)


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "order")


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ("title", "module", "order", "duration")