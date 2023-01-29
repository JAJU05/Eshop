from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = 'contact.html'


class AuthView(TemplateView):
    template_name = 'login_register.html'
