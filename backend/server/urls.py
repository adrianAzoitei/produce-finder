from django.urls import path

from . import views

urlpatterns = [
    # TODO: add uid path parameter
    path("detect", views.detect, name="detect"),
]