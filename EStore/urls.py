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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("account/", include('accounts.urls', namespace='accounts')),
    path("vendor/", include("vendors.urls", namespace="vendor")),
    path("product/", include("products.urls", namespace="product")),
    path("category/", include("category.urls", namespace="category")),
    path("cart/", include("carts.urls", namespace="cart")),
    path("orders/", include('orders.urls', namespace="order")),
    path("about_us/", views.about_us, name="about_us"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path("terms_condition/", views.terms_condition, name="terms_condition"),
    path("payment_policy/", views.payment_policy, name="payment_policy"),
    path("shipping_policy/", views.shipping_policy, name="shipping_policy"),
    path("return_policy/", views.return_policy, name="return_policy")



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)