from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import UserProfile, Order


@receiver(post_save, sender=User, dispatch_uid="create_user_profile")
def create_user_profile(sender, instance, **kwargs):
    print("**** signal received")
    print(sender)
    print(kwargs)
    if not UserProfile.objects.filter(user=instance).exists():
        user_profile = UserProfile()
        user_profile.user = instance
        user_profile.save()


@receiver(post_save, sender=Order, dispatch_uid="create_order")
def create_order(sender, instance, **kwargs):
    print("**** order created")
    print(sender)
    print(kwargs)
    if not Order.objects.exists():
        order = Order()
        order.order_id = instance
        order.save()
