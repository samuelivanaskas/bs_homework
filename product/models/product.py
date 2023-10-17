# product/models/product_views.py
from django.db import models


class Product(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField(null=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField('ProductCategory', blank=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    objects = models.Manager()
