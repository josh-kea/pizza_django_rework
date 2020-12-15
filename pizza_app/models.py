from uuid import uuid4
from django.contrib.auth.models import User
from django.db import models
import random, _datetime

# new
# Adds UserProfile model to Pizza app instead
# Easier to manage

# CHANNELS FOR WHEN ORDER IS PLACED
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


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
        user = None
        # Creating a new Django user and also referencing this new user in a variable to be used later down when creating a user profile
        user = User.objects.create_user(
            username=username, password=password, email=email)

        userProfile = cls()
        userProfile.user = user
        userProfile.telephone = telephone
        # Hardcoded testing creating user with customer status so we can test further and improve
        userProfile.user_status = "customer"
        userProfile.save()

        return user

    def __str__(self):
        return f'{self.user}'


class Pizza(models.Model):
    pizza_id = models.IntegerField(null=False, default="0")
    name = models.CharField(max_length=250)
    text = models.CharField(max_length=250)
    price = models.IntegerField(default=0)

    @classmethod
    def create(cls, pizza_id, name, text, price):
        pizza = cls()
        pizza.pizza_id = random.randint(100000, 400000)
        pizza.name = name
        pizza.text = text
        pizza.price = price
        pizza.save()

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    status = (
        ('pending', 'pending'),
        ('delivering', 'delivering'),
        ('delivered', 'delivered'),
    )

    # order_id = models.IntegerField(null=False, default="0")
    order_date_time = models.DateTimeField(auto_now_add=True)
    delivery_date_time = models.DateTimeField(default='20:00')
    total_price = models.IntegerField(default=0)
    order_status = models.CharField(
        choices=status, default='pending', max_length=250)
    pizzas = models.CharField(max_length=250, default="Pepperoni")

    @classmethod
    def create(cls, delivery_date_time, pizza_id, pizza_name, pizza_price):
        order = cls()
        # order.order_id = random.randint(100000, 400000)
        # order.order_date_time = order_date_time
        order.delivery_date_time = delivery_date_time
        order.total_price = pizza_price
        #order.order_status = order_status

        order.pizzas = pizza_name
        order.save()

        order.create_order_notification()
        order.test_print()

        return order

    def create_order_notification(self):
        # current_user = request.user # Getting current user
        # current_user = user = "Test"
        channel_layer = get_channel_layer()
        data = "Order #"+ str(self.pk) + " placed." # Pass any data based on your requirement
        # Trigger message sent to group
        async_to_sync(channel_layer.group_send)(
            str("Order_Notification_Group"),  # Group Name, Should always be string
            {
                "type": "notify",   # Custom Function written in the consumers.py
                "text": data,
            },
        )

    def test_print(self):
        print("Testing the print method. Order id: #" + str(self.pk))

    def __str__(self):
        return f"Order #{self.order_id} - Pizzas: {self.pizzas}"

        # simple responsibility principles



