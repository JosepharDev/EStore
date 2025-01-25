from django.http import HttpResponse
from django.shortcuts import render
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