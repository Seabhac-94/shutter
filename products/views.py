from django.shortcuts import render
from .models import Product

# Create your views here.

"""
Displays collections.html
"""

def collections(request):
    return render(request, 'collections.html')

"""
Displays all products
"""
def all_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {"products":products})

"""
Views that diplay the photos according to photo_type, ie. collections
"""
def still_life_products(request):
    products = Product.objects.filter(photo_type='Still Life')
    return render(request, 'products.html', {"products":products})

def adventure_products(request):
    products = Product.objects.filter(photo_type='Adventure')
    return render(request, 'products.html', {"products":products})

def nature_products(request):
    products = Product.objects.filter(photo_type='Nature')
    return render(request, 'products.html', {"products":products})

def irishness_products(request):
    products = Product.objects.filter(photo_type='Irishness')
    return render(request, 'products.html', {"products":products})
    