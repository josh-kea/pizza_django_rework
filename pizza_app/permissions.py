from rest_framework import permissions
from django.contrib.auth.models import User
from .models import UserProfile

class IsEmployeeOrNoAccess(permissions.BasePermission):

   def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # userProfile = User.objects.get(user=request.user)
        # if userProfile.status == 'employee':
        #     return obj.user == request.user