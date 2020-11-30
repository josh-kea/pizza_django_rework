from django.contrib.auth.models import User
from django.db import models
import random


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
