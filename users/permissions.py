from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow users to view/edit their own data.
    """
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class IsAdminUser(permissions.BasePermission):
    """
    Permission to only allow access to admin users.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_staff