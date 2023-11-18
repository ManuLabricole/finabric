from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from .models import CustomUser, UserProfile
from .serializers import UserRegistrationSerializer


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

    def test_number_validator(self):
        user = CustomUser(email="testuser")
        with self.assertRaises(ValidationError):
            user.set_password("ADinozedSD*")
            user.full_clean()

    def test_uppercase_validator(self):
        user = CustomUser(email="testuser")
        with self.assertRaises(ValidationError):
            user.set_password("adinozedsd*")
            user.full_clean()

    def test_lowercase_validator(self):
        user = CustomUser(email="testuser")
        with self.assertRaises(ValidationError):
            user.set_password("ADINOZEDSD*")
            user.full_clean()


class CustomUserAndProfileTest(TestCase):
    def setUp(self):
        # This method will run before every test
        self.user_data = {
            "email": "testuser@example.com",
            "password": "Testpass123!",
            # "first_name": "Test",
            # "last_name": "User",
        }

    def test_user_and_profile_creation_with_full_data(self):
        data = {
            "email": "test@example.com",
            "password": "strongpassword123",
            "first_name": "Test",
            "last_name": "User",
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        user = serializer.save()

        # Check if CustomUser is created
        self.assertIsNotNone(CustomUser.objects.get(email="test@example.com"))

        # Check if UserProfile is created
        self.assertIsNotNone(UserProfile.objects.get(user=user))

        # # Check the data
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.first_name, "Test")
        self.assertEqual(profile.last_name, "User")

    def test_invalid_data_handling(self):
        data = {
            "email": "notanemail",
            "password": "weak",
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_duplicate_email_rejection(self):
        CustomUser.objects.create_user(**self.user_data)
        serializer = UserRegistrationSerializer(data=self.user_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_profile_creation_without_optional_fields(self):
        data = {
            "email": "optional@example.com",
            "password": "Testpass123!",
        }
        serializer = UserRegistrationSerializer(data=data)
        self.assertTrue(serializer.is_valid())

        user = serializer.save()

        # Assertions
        profile = UserProfile.objects.get(user=user)
        self.assertEqual(profile.first_name, "")
        self.assertEqual(profile.last_name, "")
