from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    slug = models.SlugField()
    order = models.BooleanField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse('category:category_view')
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "categories"

class CategoryImage(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    Category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='category/image')
    slug = models.SlugField()
    featured_image = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.title
    

    def get_cat_url(self):
        return reverse('category:category', args={self.slug})