from django.db import models
from django.utils import timezone


class Product(models.Model):
    # tag_set = models.ManyToManyField(to=Tag)
    # seller = models.ForeignKey(to=Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    sku = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    created_at = models.DateTimeField('date created', default=timezone.now)
    updated_at = models.DateTimeField('date updated', default=timezone.now)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
