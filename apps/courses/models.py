from django.conf import settings
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=1)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['position']
        unique_together = ('course', 'position')

    def __str__(self) -> str:
        return f'{self.course.title}: {self.title}'


class LessonMaterial(models.Model):
    class MaterialType(models.TextChoices):
        VIDEO = 'video', 'Video'
        DOCUMENT = 'document', 'Document'
        LINK = 'link', 'Link'

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    material_type = models.CharField(max_length=20, choices=MaterialType.choices)
    url = models.URLField()

    def __str__(self) -> str:
        return f'{self.lesson.title}: {self.title}'
