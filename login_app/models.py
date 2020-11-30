from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe


class PasswordResetRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    secret = models.CharField(max_length=43, default=token_urlsafe)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} - {self.created_timestamp}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone_number = models.IntegerField(default=12345678)
    status = (
        ('employee', 'employee'),
        ('user', 'user')
    )
    user_status = models.CharField(
        choices=status, default='user', max_length=250)

    def __str__(self):
        return f'{self.user}'
