from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from . models import UserProfile, Order


@receiver(post_save, sender=User, dispatch_uid="create_user_profile")
def create_user_profile(sender, instance, **kwargs):
    print("**** signal received")
    print(sender)
    print(kwargs)


@receiver(post_save, sender=Order, dispatch_uid="create_order")
def create_order(sender, instance, **kwargs):
    print("**** Order created #"+ Order.pk)
    print(sender)
    print(kwargs)
    