from django.contrib import admin
from django.urls import path
from .views.home import home

urlpatterns = [
    path('', home),
]
