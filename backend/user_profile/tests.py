from django.test import TestCase

# Create your tests here.
# tests.py in your user_profile app

import json

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User


class RegistrationTestCase(APITestCase):
    def test_registration_success(self):
        # Define a valid payload to send to the registration endpoint
        data = {
            "username": "newuser",
            "password": "Newpass123!",
            "email": "newuser@example.com",
            "firstname": "New",
            "lastname": "User"
            # Include other fields required for UserProfile
        }
        response = self.client.post(reverse("user-profile-register"), json.dumps(data), content_type="application/json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("newuser" in response.data["message"])

    # def test_registration_with_existing_email(self):
    #     # Create a user to test against
    #     User.objects.create_user("testuser", "test@example.com", "password123")

    #     # Try to register another user with the same email
    #     data = {
    #         "username": "testuser2",
    #         "password": "password123",
    #         "email": "test@example.com",
    #         # ... other required fields ...
    #     }
    #     response = self.client.post(reverse("register"), data)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertTrue("email" in response.data)

    # def test_registration_with_weak_password(self):
    #     # Payload with a weak password (no special characters)
    #     data = {
    #         "username": "weakpassworduser",
    #         "password": "password",
    #         "email": "weakpassuser@example.com",
    #         # ... other required fields ...
    #     }
    #     response = self.client.post(reverse("register"), data)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertTrue("password" in response.data)
