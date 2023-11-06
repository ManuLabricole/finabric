from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from user_profile.views import CustomRegistrationView


urlpatterns = [
    path(
        "api/v1/register/",
        CustomRegistrationView.as_view(),
        name="user-profile-register",
    ),
]
