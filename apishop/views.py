from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apishop.models import Product

class ProductView(APIView):

 def get(self, request, format=None):
    product_names = [product.name for product in Product.objects.all()]
    return Response(product_names)
