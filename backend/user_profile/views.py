from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    CustomUserRegistrationSerializer,
)  # assuming you created a custom serializer


class CustomRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(
                    {"message": "User created successfully."},
                    status=status.HTTP_201_CREATED,
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
