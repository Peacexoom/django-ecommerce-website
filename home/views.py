from unicodedata import category
from django.shortcuts import render
from products.models import Product, Category

def home(request):
    context = {
        'men_products': Product.objects.filter(category__category_name='Men'),
        'women_products': Product.objects.filter(category__category_name='Women')
    }
            
    return render(request, 'home/home.html', context)