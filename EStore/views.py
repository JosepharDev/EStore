from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Product
from category.models import Category, CategoryImage

def index(request):
    cat = Category.objects.all()
    cat_image = CategoryImage.objects.filter(Category_id__in=cat)[:4]
    featured_prod = Product.objects.filter(featured=True).order_by('-featured')[:7]
    recent_prod = Product.objects.filter(recent_product=True).order_by('-recent_product')[:7]
    context = {
        "cat_image": cat_image,
        'featured': featured_prod,
        'recent_prod': recent_prod
    }
    return render(request,'index.html', context)

def about_us(request):
    return render(request, 'about_us.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms_condition(request):
    return render(request, "terms_condition.html")

def payment_policy(request):
    return render(request, "payment_policy.html")

def shipping_policy(request):
    return render(request, "shipping_policy.html")

def return_policy(request):
    return render(request, "return_policy.html")