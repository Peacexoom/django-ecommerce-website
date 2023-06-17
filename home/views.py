# from unicodedata import category
from django.shortcuts import render, redirect
from products.models import Product

def home(request):
    if request.user.is_anonymous:
        return redirect("/userauth/login")
    
    user = request.user
    
    context = {
        'user': user,
        'men_products': Product.objects.filter(category__category_name='Men'),
        'women_products': Product.objects.filter(category__category_name='Women')
    }
            
    return render(request, 'home/home.html', context)