from django.test import TestCase
from django.core.exceptions import ValidationError

from django.test import TestCase
from .models import CustomUser


class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email="user@example.com", password="testpass123"
        )
        self.assertEqual(user.email, "user@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = CustomUser.objects.create_superuser(
            "admin@example.com", "admin123"
        )
        self.assertEqual(admin_user.email, "admin@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)




class PasswordValidatorTest(TestCase):
    def test_special_character_validator(self):
        user = CustomUser(email="testuser")
        with self.assertRaises(ValidationError):
            user.set_password("passwordWithoutSpecialChar")
            user.full_clean()
