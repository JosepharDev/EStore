from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remote_cart, name='remove_cart'),
    path('checkout/', views.checkout, name="checkout"),
]
