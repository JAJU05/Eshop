from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse_lazy
from django.views.generic import FormView


class User(AbstractUser):
    email = EmailField(max_length=255, unique=True),
    phone = CharField(max_length=25, null=True, blank=True),

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'


class RegistrationView(FormView):
    template_name = 'login_register.html'
    success_url = reverse_lazy('index')


# class LoginPageView(LoginView):
#     fields = '__all__'
#     template_name = 'login_register.html'
