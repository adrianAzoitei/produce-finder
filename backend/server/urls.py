from django.urls import path

from . import views

urlpatterns = [
    # TODO: add uid path parameter
    path("detect/<uuid:user_id>/", views.detect, name="detect"),
]