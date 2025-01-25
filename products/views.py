from django.shortcuts import render, get_object_or_404
from vendors.mixins import VendorMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Product
from .forms import ProductFrom
from django.db.models import Q
from itertools import chain
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponse
from .mixins import ProductUpdateMixin
from EStore.mixins import MultiSlugMixin
from carts.models import CartItem
from carts.views import _cart_id
from vendors.models import Vendor
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
    if request.user.is_authenticated:
        in_cart = CartItem.objects.all().filter(user=request.user, product=product).exists()
    else:
        in_cart = CartItem.objects.all().filter(cart__cart_id=_cart_id(request), product=product).exists()
    related_product = Product.objects.filter(category=product.category).exclude(slug=product.slug)
    context = {
        'product': product,
        'related_product': related_product,
        'in_cart': in_cart,
    }
    return render(request, 'products/product_detail.html', context)

def search_view(request, *args, **kwargs):
    try:
        q = request.GET.get('q','')
    except:
        q = False
    obj = Product.objects.filter(Q(title__icontains=q)|Q (description__icontains=q) | Q(category__title__icontains=q)).order_by('id')
    results = list(chain(obj))
    paginator = Paginator(results, 2)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'results': paged_products,
        'obj': obj,
        'q': q,
    }
    return render(request, "products/search_result.html", context)


class ProductUpdateView(ProductUpdateMixin, VendorMixin, UpdateView):
    model = Product
    form_class = ProductFrom
    template_name = 'products/update_view.html'
    success_url = '/'



class VendorListView(ListView):
    model = Product
    template_name = 'products/product_list.html'

    def get_object(self, *args, **kwargs):
        seller_name = self.kwargs.get('vendor_name')
        seller = get_object_or_404(Vendor, seller__username=seller_name)
        return seller

    def get_context_data(self, *args, **kwargs):
        context = super(VendorListView, self).get_context_data(*args, **kwargs)
        context['vendor_name'] = str(self.get_object().seller.username)
        return context

    def get_queryset(self, **kwargs):
        seller = self.get_object()
        qs = super(VendorListView, self).get_queryset(**kwargs).filter(seller=seller)
        return qs
    