from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == "list":
            return request.user.is_authenticated or request.user.is_superuser
        elif view.action == "create":
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if view.action == "retrieve":
            return obj == request.user or request.user.is_superuser
        elif view.action in ["update", "partial_update"]:
            return obj == request.user or request.user.is_superuser
        elif view.action == "destroy":
            return request.user.is_superuser
        else:
            return False
