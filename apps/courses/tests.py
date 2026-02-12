from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Course, Lesson, LessonMaterial


class CourseModelsTests(TestCase):
    def setUp(self):
        self.teacher = get_user_model().objects.create_user(username='teacher1', password='test-pass')

    def test_course_lesson_and_material_relations(self):
        course = Course.objects.create(title='Алгебра', description='Базовый курс', teacher=self.teacher)
        lesson = Lesson.objects.create(course=course, title='Уравнения', position=1)
        material = LessonMaterial.objects.create(
            lesson=lesson,
            title='Видео по уравнениям',
            material_type=LessonMaterial.MaterialType.VIDEO,
            url='https://example.com/video',
        )

        self.assertEqual(str(course), 'Алгебра')
        self.assertEqual(str(lesson), 'Алгебра: Уравнения')
        self.assertIn('Видео по уравнениям', str(material))
        self.assertEqual(course.lessons.count(), 1)
        self.assertEqual(lesson.materials.count(), 1)


class CourseListViewTests(TestCase):
    def test_course_list_page_is_available(self):
        response = self.client.get(reverse('courses:course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Курсы')
