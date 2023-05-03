from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.is_active and user.is_staff
