from django.urls import path

from . import views

urlpatterns = [
    path("scooby", views.index, name="index"),
]