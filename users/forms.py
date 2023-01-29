from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, EmailField, CharField
from django.core.exceptions import ValidationError

from users.models import User


class AuthLoginForm(Form):
    email = EmailField(max_length=25)
    password = CharField(max_length=255)

    # def clean_email(self):
    #     email = self.data.get('email')
    #     if not User.objects.filter(email=email).exists():
    #         raise ValidationError("This user didn't registered !")
    #     return email


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(max_length=255)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Account with this email already exists")
        return email

    class Meta:
        model = User
        fields = ('email',)
        field_classes = None
