import uuid

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        email = email.lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # Overriding the 'groups' field
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions granted to each of their groups."
        ),
        related_name="customuser_groups",
        related_query_name="customuser",
    )

    # Overriding the 'user_permissions' field
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="customuser_user_permissions",
        related_query_name="customuser",
    )


from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from PIL import Image


class UserProfile(models.Model):
    # Link to the CustomUser model
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )

    # Additional fields
    avatar = models.ImageField(
        upload_to="avatars/", default="avatars/default.jpg", blank=True
    ) # This indicate a subdirectory of the MEDIA_ROOT directory to store the uploaded file
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(18)])
    monthly_income = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    monthly_expenses = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    saving_profile = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.email}'s profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Handle image resizing
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.avatar.path)
