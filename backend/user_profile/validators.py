# validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _  # Updated import


class SpecialCharacterValidator(object):
    def validate(self, password, user=None):
        if not any(char in password for char in "!@#$%^&*()"):
            raise ValidationError(
                _("The password must contain at least one special character."),
                code="password_no_special",
            )

    def get_help_text(self):
        return _("Your password must contain at least one special character.")
