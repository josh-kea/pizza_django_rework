from django.shortcuts import render, get_object_or_404, reverse
from login_app.models import UserProfile
from .models import Pizza
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import random
# Create your views here.


@login_required
def index(request):
    pizzas = Pizza.objects.all()
    userProfiles = UserProfile.objects.filter(user=request.user)
    context = {
        'pizzas': pizzas,
        'userProfiles': userProfiles,
    }
    return render(request, 'pizza_app/index.html', context)


@login_required
def employe_page(request):
    if request.method == 'POST':
        name = request.POST['pizza_name']
        text = request.POST['pizza_text']
        price = request.POST['pizza_price']
        pizza = Pizza()
        pizza.name = name
        pizza.text = text
        pizza.price = price
        pizza.save()
    pizzas = Pizza.objects.all()
    userProfiles = UserProfile.objects.filter(user=request.user)
    context = {
        'pizzas': pizzas,
        'userProfiles': userProfiles,
    }
    return render(request, 'pizza_app/employe_page.html', context)


@login_required
def base(request):
    userProfiles = UserProfile.objects.filter(user=request.user)
    context = {
        'userProfiles': userProfiles,
    }
    return render(request, 'pizza_app/base.html', context)


@login_required
def edit_pizza(request):
    pizzas = Pizza.objects.all()
    userProfiles = UserProfile.objects.filter(user=request.user)
    context = {
        'pizzas': pizzas,
        'userProfiles': userProfiles,
    }
    return render(request, 'pizza_app/edit_pizza.html', context)
