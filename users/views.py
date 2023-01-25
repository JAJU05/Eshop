from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from users.mixins import AuthUserMixin
from users.forms import AuthLoginForm, CustomUserCreationForm
from django.contrib.auth.views import FormView, TemplateView


class CustomLoginView(AuthUserMixin, FormView):
    form_class = AuthLoginForm
    success_url = reverse_lazy('index')
    template_name = 'login_register.html'

    def form_valid(self, form):
        user = authenticate(**form.data.dict())
        if user:
            login(self.request, user)
            return super().form_valid(form)
        form.add_error('password', "Please type the correct password")  # is_active or incorrect password error
        return super().form_invalid(form)


class RegisterView(AuthUserMixin, FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'login_register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
