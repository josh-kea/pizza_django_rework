from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
import random

class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    status = (
        ('employee', 'employee'),
        ('customer', 'customer')
    )
    user_status = models.CharField(
        choices=status, default='customer', max_length=250)

    def __str__(self):
        return f'{self.user}({self.user_status})'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    user_type = models.ForeignKey(UserType, on_delete=models.PROTECT)
    telephone = models.CharField(max_length=35)

    @classmethod
    def create_user(cls, username, password, email, telephone) -> User:
        user = User.objects.create_user(username=username, password=password, email=email)
        cls(user=user, telephone=telephone).save()
        userProfile.user = user
        userProfile.telephone = telephone
        userProfile.save()
        return user

    def __str__(self):
        return f'{self.user}'



class Pizza(models.Model):
    pizza_id = random.randint(100000, 400000)
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    price = models.IntegerField(default=0)

    @classmethod
    def create(cls, pizza_id, name, text, price):
        pizza = cls()
        pizza.pizza_id = pizza_id
        pizza.name = name
        pizza.text = text
        pizza.price = price
        pizza.save()

    def __str__(self):
        return f"{self.name}"
