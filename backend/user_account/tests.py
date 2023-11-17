from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError

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

    def test_email_normalization(self):
        user = CustomUser.objects.create_user(
            email="TestEmail@Example.Com", password="testpass123"
        )
        print(user.email)
        self.assertEqual(user.email, "testemail@example.com")

    def test_user_string_representation(self):
        user = CustomUser.objects.create_user(
            email="user@example.com", password="testpass123"
        )
        self.assertEqual(str(user), user.email)

    def test_user_password_change(self):
        user = CustomUser.objects.create_user(
            email="user@example.com", password="old_password"
        )
        user.set_password("new_password")
        self.assertTrue(user.check_password("new_password"))

    def test_duplicate_email(self):
        CustomUser.objects.create_user(email="user@example.com", password="testpass123")
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create_user(
                email="user@example.com", password="testpass456"
            )

    def test_required_fields(self):
        user = CustomUser.objects.create_user(
            email="user@example.com", password="testpass123"
        )
        self.assertIsNotNone(user.email)


class PasswordValidatorTest(TestCase):
    def test_special_character_validator(self):
        user = CustomUser(email="testuser")
        with self.assertRaises(ValidationError):
            user.set_password("ADino1546zedSD")
            user.full_clean()
