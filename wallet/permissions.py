from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Права пользователя на объект
    """
    message = 'Access denied.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user