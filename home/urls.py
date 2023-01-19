from django.urls import path

from home.views import IndexListView

urlpatterns = [

    path("", IndexListView.as_view(), name="index"),
]
