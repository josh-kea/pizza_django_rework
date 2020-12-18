from rest_framework import permissions
from django.contrib.auth.models import User
from .models import UserProfile

class IsEmployeeOrNoAccess(permissions.BasePermission):
    """
    Global permission check if user is employee
    """

    def has_permission(self, request, view):
        userprofile = UserProfile.objects.get(user=request.user)

        if userprofile.user_status is 'employee':
            print(str(request.user.username) + " has permission to view " + str(view))
            return true