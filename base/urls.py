from django.urls import path
from . import views

urlpatterns = [
    path("", views.endpoints),
    path("post", views.post)
]