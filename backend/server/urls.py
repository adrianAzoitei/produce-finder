from django.urls import path

from . import views

urlpatterns = [
    path("detect", views.detect, name="detect"),
]