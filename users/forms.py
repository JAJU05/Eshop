from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, EmailField, CharField
from django.core.exceptions import ValidationError

from users.models import User


class AuthLoginForm(Form):
    email = EmailField(max_length=25)
    password = CharField(max_length=255)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError("This user didn't registered !")
        return email


class CustomUserCreationForm(UserCreationForm):
    first_name = CharField(max_length=255)

    class Meta:
        model = User
        fields = ('email',)
        field_classes = None

