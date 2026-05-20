from rest_framework import generics
from .models import (
    category,
    product,
)

from .serializers import (
    ProductSerializer,
    CategorySerializers
)

class ProductListView(generics.ListAPIView):
    queryset = product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    filterset_fields = ['category']
    search_fields = ['title', 'price','description']

class ProductDetailView(generics.RetrieveAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class CategoryListView(generics.ListAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializers