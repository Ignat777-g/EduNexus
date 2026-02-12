from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import UserProfile


class UserProfileTests(TestCase):
    def test_profile_string_representation(self):
        user = get_user_model().objects.create_user(username='student1', password='test-pass')
        profile = UserProfile.objects.create(user=user, role=UserProfile.Role.STUDENT)

        self.assertEqual(str(profile), 'student1 (student)')
