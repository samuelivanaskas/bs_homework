from django.urls import path, include
from rest_framework import routers

from product import viewsets

router = routers.SimpleRouter()
router.register(r'product', viewsets.ProductViewSets, basename='product')
router.register(r'category', viewsets.CategoryViewSets, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
