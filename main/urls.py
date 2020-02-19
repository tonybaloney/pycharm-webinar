from django.contrib import admin
from django.urls import path
from .views.home import home
from .views.admin import admin_home

urlpatterns = [
    path('', home),
    path('admin', admin_home)
]
