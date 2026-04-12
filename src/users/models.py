from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE = (
        ('admin', 'Admin'),
        ('seller', 'Seller'),
        ('customer', 'Customer'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPE)
    phone = models.CharField(max_length=15, blank=True, null=True, unique=True)

    def __str__(self):
        return self.username


class BaseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AdminProfile(BaseProfile):
    permissions_level = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.user.username


class SellerProfile(BaseProfile):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class CustomerProfile(BaseProfile):
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
