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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.image:
            try:
                data['image'] = instance.image.url
            except Exception:
                data['image'] = str(instance.image)
        return data

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
        
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
