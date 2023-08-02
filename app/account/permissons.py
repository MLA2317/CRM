from rest_framework import permissions


class IsOwnUserOrReadOnly(permissions.BasePermission):
    "Is_Owner"
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.phone == request.user.phone


class IsAdminUserForAccount(permissions.IsAdminUser):
    "Is_admin"
    def has_permission(self, request, view):
        return bool(request.user.is_staff or request.user.is_superuser)


class IsAuthenticated(permissions.IsAuthenticated):
    "Is_authenticate"
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user or request.user.is_student or request.user.is_teacher)
