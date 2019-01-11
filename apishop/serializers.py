from apishop.models import Product, Category
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'description', 'sku', 'price','image','slug','description','price','available','created_at', 'updated_at','category')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name', 'slug', 'created_at', 'updated_at')
