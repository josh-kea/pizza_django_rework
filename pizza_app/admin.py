from django.contrib import admin
from .models import UserProfile, Pizza, Order  # new

admin.site.register(UserProfile)  # Registers user profile here instead
admin.site.register(Pizza)
admin.site.register(Order)

# Register your models here.
