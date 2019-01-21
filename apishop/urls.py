"""tproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf.urls import url
from apishop.views import ProductView, ProductDetailView, CategoryView, CategoryDetailView, CartView, CartCreateView

urlpatterns = [
    url(r'^product/(?P<pk>\d+)/$', ProductDetailView.as_view(), name="user_detail"),
    url(r'^category/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name="category_detail"),
    path('product', ProductView.as_view()),
    path('category', CategoryView.as_view()),
    path('cart', CartView.as_view()),
    path('cart/create', CartCreateView.as_view())
]