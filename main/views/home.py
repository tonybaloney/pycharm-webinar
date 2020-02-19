from django.shortcuts import render
from ..models import Product, Promotions
from django.utils.safestring import mark_safe

def home(request):
    products = Product.objects.all()
    promotions = Promotions.objects.all()
    promo = mark_safe(promotions[0].details)
    return render(request, "home.html", context={"products": products, "request": request, "promotion": promo})
