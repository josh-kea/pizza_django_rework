from django.contrib import admin
from .models import UserProfile, Pizza #new

admin.site.register(UserProfile) # Registers user profile here instead
admin.site.register(Pizza)


# Register your models here.
