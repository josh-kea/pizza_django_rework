from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from . import models
from pizza_app.models import UserProfile

# EMAILS
import django_rq
from . messaging import email_message

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        userProfile = UserProfile.objects.get(user=user) # Finds user profile and references in variable to be used below

        # If a user is matched
        if user: 
            if userProfile.user_status != 'employee':
                dj_login(request, user)
                return HttpResponseRedirect(reverse('pizza_app:customer_page')) # new
            elif UserProfile.user_status != 'customer':
                dj_login(request, user)
                return HttpResponseRedirect(reverse('pizza_app:employee_page')) # new
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


def request_password_reset(request):
   if request.method == "POST":
      post_user = request.POST['username']
      user = None

      if post_user:
            try:
               user = User.objects.get(username=post_user)
            except:
               print(f"Invalid password request: {post_user}")
      else:
            post_user = request.POST['email']
            try:
               user = User.objects.get(email=post_user)
            except:
               print(f"Invalid password request: {post_user}")
      if user:
            prr = PasswordResetRequest()
            prr.user = user
            prr.save()
            django_rq.enqueue(email_message, {
               'token' : prr.token,
               'email' : prr.user.email,
            })
            return HttpResponseRedirect(reverse('login_app:password_reset'))

   return render(request, 'login_app/request_password_reset.html')


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


# signup naming changed
def signup(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email = request.POST['email']
        telephone = request.POST['telephone_number']

        if password == confirm_password:
            # New try function, to try creating a new user via the userProfile @classmethod create_user . Remember inside this @classmethod we are creating the Django User object too.
            try:
                UserProfile.create_user(username, password, email, telephone)
                return HttpResponseRedirect(reverse('login_app:login'), context)

            # If the try fails then send context that we could not create a user account
            except IntegrityError:
                context['error'] = 'Could not create user account.'
        else:
            # If passwords do not match.
            context = {'error': 'Passwords do not match.'}
    return render(request, 'login_app/signup.html', context)




def delete_account(request):
    pass
