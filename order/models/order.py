# order/models/order.py

from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    objects = None
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
