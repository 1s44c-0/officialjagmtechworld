from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class category(models.Model):
    name = models.CharField(
        max_length = 255
    )

    def __str__(self):
        return self.name

class product(models.Model):
    category = models.ForeignKey(
        category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    title = models.CharField(
        max_length = 255
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True   
    )

    def __str__(self):
        return self.title

class productImage(models.Model):
    product = models.ForeignKey(
        product,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = CloudinaryField(
        'image'
    )

    def __str__(self):
        return f"Image for {self.product.title}"
