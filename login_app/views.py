from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import models
from .models import UserProfile


def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        userProfile = UserProfile.objects.get(user=user)
        if user:
            if userProfile.user_status != 'employee':
                dj_login(request, user)
                return HttpResponseRedirect(reverse('pizza_app:index'))
            elif UserProfile.user_status != 'user':
                dj_login(request, user)
                return HttpResponseRedirect(reverse('pizza_app:employe_page'))
        else:
            context = {'error': 'Bad username or password.'}
    return render(request, 'login_app/login.html', context)


def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('login_app:login'))


def password_reset(request):
    context = {}

    if request.method == "POST":
        email = request.POST['email']
        user = User.objects.get(email=email)
        reset_request = models.PasswordResetRequest()
        reset_request.user = user
        reset_request.save()
        url = reverse('login_app:password_reset_secret',
                      args=[f'{reset_request.secret}'])
        url = f'{request.scheme}://{request.META["HTTP_HOST"]}{url}'
        print(url)
        context = {
            'message': 'Please click the link in the email we sent to you.'}

    return render(request, 'login_app/password_reset.html', context)


def password_reset_secret(request, secret):
    context = {'secret': secret}
    return render(request, 'login_app/password_reset_form.html', context)


def password_reset_form(request):
    email = request.POST['email']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    secret = request.POST['secret']
    user = User.objects.get(email=email)
    reset_request = models.PasswordResetRequest.objects.get(
        user=user, secret=secret)
    if password == confirm_password:
        user.set_password(password)
        user.save()
        reset_request.save()
        return HttpResponseRedirect(reverse('login_app:login'))
    context = {
        'error': 'Something went wrong, try again, don\'t screw up this time!'}
    return render(request, 'login_app/password_reset_form.html', context)


def sign_up(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        if password == confirm_password:
            if User.objects.create_user(username, email, password):
                return HttpResponseRedirect(reverse('login_app:login'))
            else:
                context = {
                    'error': 'Could not create user - try somethig else.'}
        else:
            context = {'error': 'Passwords do not match.'}
    return render(request, 'login_app/sign_up.html', context)


def user_profile(request):
    userProfiles = UserProfile.objects.filter(user=request.user)
    context = {
        'userProfiles': userProfiles,
    }
    return render(request, 'login_app/user_profile.html', context)


def delete_account(request):
    pass
