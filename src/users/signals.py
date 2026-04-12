from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User, AdminProfile, SellerProfile, CustomerProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.user_type == 'admin':
        AdminProfile.objects.create(user=instance)
    elif instance.user_type == 'seller':
        SellerProfile.objects.create(user=instance)
    elif instance.user_type == 'customer':
        CustomerProfile.objects.create(user=instance)
