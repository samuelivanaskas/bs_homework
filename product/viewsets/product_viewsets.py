from rest_framework.viewsets import ModelViewSet

from product.models import Product
from product.serializers.product_serializers import ProductSerializer


class ProductViewSets(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
