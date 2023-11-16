import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class RegistrationTestCase(APITestCase):
    def test_registration_success(self):
        # Define a valid payload to send to the registration endpoint
        data = {
            "password": "Newpass123!",
            "email": "newuser@example.com",
            "firstname": "New",
            "lastname": "User",
        }
        response = self.client.post(
            reverse("register"),
            json.dumps(data),
            content_type="application/json",
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("User created successfully" in response.data["message"])

    def test_registration_with_existing_email(self):
        # Create a user to test against
        User.objects.create_user("testuser", "test@example.com", "password123")

        # Try to register another user with the same email
        data = {
            "password": "Newpass123!",
            "email": "test@example.com",
            "firstname": "New",
            "lastname": "User",
        }
        response = self.client.post(
            reverse("register"),
            json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("email" in response.data)

    def test_registration_with_weak_password(self):
        # Payload with a weak password (no special characters)
        data = {
            "password": "password!",
            "email": "test@example.com",
            "firstname": "New",
            "lastname": "User",
        }
        response = self.client.post(
            reverse("register"), json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("password" in response.data)

    def test_registration_with_missing_fields(self):
        # Payload with missing fields
        data = {
            "password": "password!",
            "email": "user@gmail.com",
            # Missing firstname and lastname
        }
        response = self.client.post(
            reverse("register"), json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("firstname" in response.data)

    def test_registration_without_special_characters_in_password(self):
        # Payload with missing fields
        data = {
            "password": "Longpassword123",
            "email": "test@example.com",
            "firstname": "New",
            "lastname": "User",
        }
        response = self.client.post(
            reverse("register"), json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("password" in response.data)

    def test_user_and_userprofile_creation(self):
        # Define a valid payload to send to the registration endpoint
        data = {
            "password": "Newpass123!",
            "email": "newuser@example.com",
            "firstname": "New",
            "lastname": "User",
        }
        response = self.client.post(
            reverse("register"),
            json.dumps(data),
            content_type="application/json",
        )
        user = User.objects.get(email="newuser@example.com")
        self.assertEqual(user.username, "New_User")
        user_profile = user.userprofile
        self.assertEqual(user_profile.firstname, "New")


class EmailAuthBackendTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword123"
        )

    def test_authenticate_with_email(self):
        # Test authenticating with email
        user = authenticate(username="test@example.com", password="testpassword123")
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "test@example.com")

    def test_authenticate_with_username(self):
        # Test authenticating with username
        user = authenticate(username="testuser", password="testpassword123")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "testuser")

    def test_authenticate_with_incorrect_email(self):
        # Test failure with incorrect email
        user = authenticate(username="wrong@example.com", password="testpassword123")
        self.assertIsNone(user)

    def test_authenticate_with_incorrect_password(self):
        # Test failure with incorrect password
        user = authenticate(username="test@example.com", password="wrongpassword")
        self.assertIsNone(user)
