from django.contrib import admin

from .models import Course, Lesson, LessonMaterial


class LessonMaterialInline(admin.TabularInline):
    model = LessonMaterial
    extra = 0


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'position')
    list_filter = ('course',)
    inlines = (LessonMaterialInline,)


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'created_at')
    search_fields = ('title', 'teacher__username')
    list_filter = ('created_at',)
    inlines = (LessonInline,)


@admin.register(LessonMaterial)
class LessonMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson', 'material_type')
    list_filter = ('material_type',)
    search_fields = ('title', 'lesson__title')
