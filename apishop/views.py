from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apishop.models import Product, Category
from apishop.serializers import ProductSerializer, CategorySerializer
from rest_framework import generics
from rest_framework import viewsets

'''
class ProductView(APIView):
    def get(self, request, format=None):
       product_names = [product.name for product in Product.objects.all()]
       return Response(product_names)
'''
# or


class ProductView(generics.ListCreateAPIView, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer