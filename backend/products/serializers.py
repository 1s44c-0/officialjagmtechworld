from rest_framework import serializers
from .models import (
    category,
    product,
    productImage
)

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = category

        fields = [
            "id",
            "name"
        ]

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImage

        fields = [
            "id",
            "image"
        ]
        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializers(
        read_only=True
    )

    images = ProductImageSerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = product
        fields = [
            "id",
            "title",
            "price",
            "description",
            "category",
            "images",
            "created_at"
        ]
