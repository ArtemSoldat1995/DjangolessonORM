from django.shortcuts import render
from .models import *

def home(request):
    products= Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'prod_detail.html', {'product': product})
