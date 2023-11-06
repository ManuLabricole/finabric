from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from user_profile.views import UserRegistrationAPIView


urlpatterns = [
    path(
        "register/",
        UserRegistrationAPIView.as_view(),
        name="user-profile-register",
    ),
]
