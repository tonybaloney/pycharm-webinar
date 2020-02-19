from django.shortcuts import render
from ..models import Product, TemporaryUser

# Create your views here.
def admin_home(request):
    # Check this person is an administrator
    assert request.user.is_superuser
    products = Product.objects.all()
    return render(request, "admin.html", context={"products": products})

def increase_prices(request):
    Product.objects.raw("UPDATE myapp_person SET price = '%s' WHERE name = '%s'", [new_price, product])