from django.shortcuts import render
from vendors.mixins import VendorMixin
from django.views.generic.edit import CreateView
from .models import Product
from .forms import ProductFrom

# Create your views here.

class ProductCreateView(VendorMixin, CreateView):

    model = Product
    form_class = ProductFrom
    template_name = 'products/create_view.html'
    success_url = '/'

    def form_valid(self, form):
        seller = self.get_vendor()
        form.instance.seller = seller
        data = super(ProductCreateView, self).form_valid(form)
        
        return data

def product_detail(request, slug):
    obj = Product.objects.filter(slug=slug)
    product = None
    if obj.exists():
        product = obj.first()
    related_product = Product.objects.filter(category=product.category).exclude(slug=product.slug)
    context = {
        'product': product,
        'related_product': related_product
    }
    return render(request, 'products/product_detail.html', context)