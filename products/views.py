from django.shortcuts import render
from vendors.mixins import VendorMixin
from django.views.generic.edit import CreateView, UpdateView
from .models import Product
from .forms import ProductFrom
from django.db.models import Q
from itertools import chain
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from .mixins import ProductUpdateMixin
from EStore.mixins import MultiSlugMixin
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