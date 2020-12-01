from django.shortcuts import render, get_object_or_404, reverse
from .models import UserProfile, Pizza
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import random
# Create your views here.

@login_required
def user_profile(request):
    if request.method == 'GET':
        userProfile = UserProfile.objects.get(user=request.user)
        context = {
            'userProfile': userProfile,
    }
    return render(request, 'pizza_app/user_profile.html', context)



@login_required
def customer_page(request):
    pizzas = Pizza.objects.all()
    userProfiles = UserProfile.objects.filter(user=request.user)
    context = {
        'pizzas': pizzas,
        'userProfiles': userProfiles,
    }
    return render(request, 'pizza_app/customer_page.html', context)


@login_required
def employee_page(request):
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
    return render(request, 'pizza_app/employee_page.html', context)


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
