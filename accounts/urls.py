from django.urls import path, include
from django.conf.urls import url
from accounts.views import AccountCreateView
from rest_framework import routers

urlpatterns = [
    path('accounts/create', AccountCreateView.as_view()),
]