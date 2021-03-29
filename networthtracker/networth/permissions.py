from rest_framework import permissions
import logging


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to access it.
    """

    def has_object_permission(self, request, view, obj):
        logging.warning("has_object_permissions")
        return obj.user == request.user
