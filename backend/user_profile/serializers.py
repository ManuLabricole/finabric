# serializers.py
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from rest_framework import serializers


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    # Include all required fields
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("firstname", "lastname", "password", "password2", "email")

    def validate(self, data):
        # Check that the two password entries match
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password2": "Password fields must match."}
            )

        # Validate password with Django's built-in validators
        validate_password(data["password"])

        # Check for a special character in the password
        if not any(char in data["password"] for char in "!@#$%^&*()"):
            raise serializers.ValidationError(
                {"password": "Password must include at least one special character."}
            )

        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"], email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
