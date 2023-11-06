from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import transaction

from .models import UserProfile


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Profile related fields
    firstname = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    birth_date = serializers.DateField(allow_null=True, required=False)
    email = serializers.EmailField(max_length=100)
    monthly_income = serializers.IntegerField(allow_null=True, required=False)
    monthly_expenses = serializers.IntegerField(allow_null=True, required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "firstname",
            "lastname",
            "birth_date",
            "email",
            "monthly_income",
            "monthly_expenses",
        ]

    def validate_email(self, value):
        # Check if any user already exists with this email
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_password(self, value):
        # Check if password is at least 8 characters long
        validate_password(value)
        return value

    @transaction.atomic
    def create(self, validated_data):
        # Create the user
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

        # Create the user profile
        UserProfile.objects.create(
            user=user,
            firstname=validated_data["firstname"],
            lastname=validated_data["lastname"],
            birth_date=validated_data.get("birth_date"),
            monthly_income=validated_data.get("monthly_income"),
            monthly_expenses=validated_data.get("monthly_expenses"),
        )
        return user
