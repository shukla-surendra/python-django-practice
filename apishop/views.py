from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apishop.models import Product
from apishop.serializers import ProductSerializer
from rest_framework import generics
from rest_framework import viewsets

'''
class ProductView(APIView):
    def get(self, request, format=None):
       product_names = [product.name for product in Product.objects.all()]
       return Response(product_names)
'''
# or

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer