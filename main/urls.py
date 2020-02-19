from django.contrib import admin
from django.urls import path
from .views.home import home
from .views.admin import admin_home, bulk_upload, increase_prices

urlpatterns = [
    path('', home),
    path('admin', admin_home),
    path('admin/increase_prices', increase_prices),
    path('admin/bulk_upload', bulk_upload)
]
