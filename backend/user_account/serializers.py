from rest_framework import serializers
from django.db import transaction
from .models import CustomUser, UserProfile


class UserRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=150, required=False)
    last_name = serializers.CharField(max_length=150, required=False)

    class Meta:
        model = CustomUser
        fields = ["email", "password", "first_name", "last_name"]
        extra_kwargs = {"password": {"write_only": True}}

    @transaction.atomic
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )
        UserProfile.objects.create(
            user=user,
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        return user
