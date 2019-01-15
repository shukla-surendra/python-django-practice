from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from accounts.serializers import UserSerializer

# Create your views here.
class AccountCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
