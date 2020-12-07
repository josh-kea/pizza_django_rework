from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
import random

# new
# Adds UserProfile model to Pizza app instead
# Easier to manage
class UserProfile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    telephone = models.CharField(max_length=35)
    status = (
        ('employee', 'employee'),
        ('customer', 'customer')
    )
    user_status = models.CharField(
        choices=status, default='customer', max_length=250)


    @classmethod
    def create_user(cls, username, password, email, telephone) -> User:
        user = User.objects.create_user(username=username, password=password, email=email) # Creating a new Django user and also referencing this new user in a variable to be used later down when creating a user profile

        userProfile = cls()
        userProfile.user = user
        userProfile.telephone = telephone
        userProfile.user_status = "customer" #Hardcoded testing creating user with customer status so we can test further and improve
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