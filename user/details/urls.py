from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("details", views.Details , name='details'),
]
