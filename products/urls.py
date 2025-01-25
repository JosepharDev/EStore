"""
URL configuration for EStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from products.views import ProductCreateView, product_detail, ProductUpdateView, VendorListView
from . import views
from django.views.generic.base import RedirectView

app_name = 'product'

urlpatterns = [
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name='update'),
    path('product/<slug:slug>/', views.product_detail, name='detail'),
    path('search/', views.search_view, name='search'),
    path('vendor/<vendor_name>/product', VendorListView.as_view(), name='vendor_detail')
    path('vendor/', RedirectView.as_view(pattern_name='category:category_view'), name='vendor_list')
]
