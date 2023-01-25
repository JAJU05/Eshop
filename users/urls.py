from django.urls import path
from users.views import CustomLoginView, RegisterView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', CustomLoginView.as_view(), name='login'),
]
