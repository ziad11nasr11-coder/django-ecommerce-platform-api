from django.db import models
from users.models import SellerProfile


class Product(models.Model):
    seller = models.ForeignKey(
        SellerProfile,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


"""
class Order(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    status = models.CharField(
        max_length=50,
        choices=(
            ('pending', 'Pending'),
            ('paid', 'Paid'),
            ('shipped', 'Shipped'),
            ('delivered', 'Delivered'),
        ),
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
"""


class Shipment(models.Model):
    seller = models.ForeignKey(
        SellerProfile,
        on_delete=models.CASCADE,
        related_name='shipments'
    )

    reference_code = models.CharField(max_length=50, blank=True, null=True)

    status = models.CharField(
        max_length=50,
        choices=(
            ('pending', 'Pending'),
            ('in_transit', 'In Transit'),
            ('delivered', 'Delivered'),
        ),
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Shipment {self.id}"


class ShipmentItem(models.Model):
    shipment = models.ForeignKey(
        Shipment,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField()

    weight = models.FloatField()
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()

    def __str__(self):
        return self.product.name
