from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegistrationView


urlpatterns = [
    path(
        "auth/register/",
        UserRegistrationView.as_view(),
        name="register",
    ),
    path(
        "auth/login/",
        TokenObtainPairView.as_view(),
        name="login",
    ),
    path(
        "auth/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh",
    ),
]
