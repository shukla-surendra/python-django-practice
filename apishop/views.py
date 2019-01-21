from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from apishop.models import Product, Category, Cart, CartItem
from apishop.serializers import ProductSerializer, CategorySerializer, CartSerializer, CartItemSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

'''
class ProductView(APIView):
    def get(self, request, format=None):
       product_names = [product.name for product in Product.objects.all()]
       return Response(product_names)
'''
# or


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # overridden list methods
    def list(self, request):
        print(request.user)
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetailView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CartView(generics.ListCreateAPIView):
    # queryset = CartItem.objects.all() #no need to define can be overridden
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Cart.objects.filter(user=user)
        '''
        try:
            cart = Cart.objects.get(user=user)
            print(cart)
        except Cart.DoesNotExist:
            raise NotFound()
        return CartItem.objects.filter(cart=cart)
        '''
    # overridden list methods
    def list(self, request):
        print(request.user.id)
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

    # def create(self, request, *args, **kwargs):
    #   ''' I wanted to do some stuff with serializer.data here '''
    #   return super(CartItemSerializer, self).create(request, *args, **kwargs)

