from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# to substitute default User with CUstomer
'''
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
 
class CustomerManager(BaseUserManager):
 
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            with transaction.atomic():
                user = self.model(email=email, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise
 
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        return self._create_user(email, password=password, **extra_fields)


 
class Customer(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
 
    """
    email = models.EmailField(max_length=40, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
 
    objects = CustomerManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
 
    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
'''
class Address(models.Model):      
    BILLING='B'    
    SHIPPING='S'
    ADDRESS_TYPE=((BILLING,'Billing'),(SHIPPING,'Shipping'))  
    address_type=models.CharField(max_length=1, choices=ADDRESS_TYPE, verbose_name="address_type")
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', null=False)
    address = models.CharField(max_length=250)
    address_more = models.CharField(max_length=200, blank=True)   
    postal_code = models.CharField(max_length=20) 
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)      