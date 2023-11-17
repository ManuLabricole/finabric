from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# from user_profile.views import UserRegistrationAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # path(
    #     "auth/register/",
    #     UserRegistrationAPIView.as_view(),
    #     name="register",
    # ),
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
