from django.shortcuts import render, redirect
from ..models import Product, TemporaryUser
from ..forms import BulkUploadForm, PriceIncreaseForm

import yaml

# Create your views here.
def admin_home(request):
    # Check this person is an administrator
    assert request.user.is_superuser
    products = Product.objects.all()
    form = BulkUploadForm()
    priceform = PriceIncreaseForm()
    return render(request, "admin.html", context={"products": products, "bulkform": form, "priceform": priceform})

def bulk_upload(request):
    if request.method == 'POST':
        form = BulkUploadForm(request.POST)
        if form.is_valid():
            data = yaml.load(form.data)
            for p in data.records:
                new_product = Product(name=p['name'], price=p['price'], description=p['description'], quantity=p['quantity'])
                new_product.save()
            return redirect('/app/admin/')

def increase_prices(request):
    if request.method == 'POST':
        form = PriceIncreaseForm(request.POST)
        if form.is_valid():
            Product.objects.raw("UPDATE main_product SET price=price*(100.0+'%s')/100.0",
                                [form.percentage])
            return redirect('/app/admin/')
