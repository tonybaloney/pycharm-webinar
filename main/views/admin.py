from django.shortcuts import render, redirect
from ..models import Product, TemporaryUser
from ..forms import BulkUploadForm, PriceIncreaseForm

import yaml

def admin_home(request):
    # Check this person is an administrator
    assert request.user.is_staff
    products = Product.objects.all()
    form = BulkUploadForm()
    priceform = PriceIncreaseForm()
    return render(request, "admin.html", context={"products": products, "bulkform": form, "priceform": priceform})

def bulk_upload(request):
    if request.method == 'POST':
        form = BulkUploadForm(request.POST)
        if form.is_valid():
            input = form.cleaned_data['input']
            data = yaml.safe_load(input)
            for p in data['products']:
                new_product = Product(name=p['name'], price=p['price'], description=p['description'], stock=0)
                new_product.save()
            return redirect('/')

def increase_prices(request):
    if request.method == 'POST':
        form = PriceIncreaseForm(request.POST)
        if form.is_valid():
            percentage = float(form.cleaned_data['percentage'])
            Product.objects.raw("UPDATE main_product SET price=price*(100.0+'%s')/100.0",
                                [percentage])
            return redirect('/')
