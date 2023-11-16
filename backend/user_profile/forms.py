from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile


class SignupForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ("email", "firstname", "lastname", "password1")
