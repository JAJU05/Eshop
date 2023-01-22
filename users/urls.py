from django.urls import path
from users.views import CustomLoginView, RegisterView

urlpatterns = [
    path('login-register', RegisterView.as_view(), CustomLoginView.as_view(), name='login_register'),
]
