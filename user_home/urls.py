from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("appointment/", views.contact, name="contact"),
]

