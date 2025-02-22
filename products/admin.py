from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'recent_product']
    list_editable = ['featured', "recent_product"]
admin.site.register(Product, ProductAdmin)