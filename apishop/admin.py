from django.contrib import admin
from .models import Product, Category

#model admin class
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'price', 'created_at']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
