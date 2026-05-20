from django.contrib import admin
from .models import (
    category,
    product,
    productImage
)

# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = productImage
    extra = 5

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id", 
        "title",
        "price",
        "category",
        "created_at"
    ]

    list_filter = [
        "category"
    ]

    search_fields = [
        "title"
    ]

    inlines = [
        ProductImageInline
    ]
