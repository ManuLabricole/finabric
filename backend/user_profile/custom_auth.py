from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            print("User does not exist")
            return None

    def get_user(self, user_id):
        try:
            print("get_user")
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
