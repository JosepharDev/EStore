from django.shortcuts import render, redirect
from django.http import HttpResponse
from carts.models import CartItem
from .forms import OrderForm
from .models import Order
from decimal import Decimal
import datetime
# Create your views here.

def place_order(request, total=0, quantity=0):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('category:category_view')
    
    for item in cart_items:
        total += item.product.price * item.quantity
    
    tax_rate = Decimal(0.05)
    tax = (total * tax_rate)
    tax = Decimal("%.2f" %(tax))
    grand_total = tax + total + 1

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = user
            data.first_name = form.cleaned_data.get("first_name")
            data.last_name = form.cleaned_data.get("last_name")
            data.email = form.cleaned_data.get('email')
            data.phone_number = form.cleaned_data.get('phone_number')
            data.country = form.cleaned_data.get('country')
            data.address = form.cleaned_data.get('address')
            data.state = form.cleaned_data.get('state')
            data.city = form.cleaned_data.get('city')
            data.tax = tax
            data.total = grand_total
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))

            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number  = order_number
            data.save()
            order = Order.objects.get(user=user, is_ordered=False, order_number=order_number)
            context = {
                'order' : order,
                'grand_total': grand_total,
                'tax': tax,
                'total': total,
                "cart_items": cart_items
            }
            return render(request, 'orders/place_order.html', context)
        else:
            return redirect("cart:checkout")

