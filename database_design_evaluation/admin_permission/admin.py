import rest_framework
from rest_framework.permissions import BasePermission


class AdminAuthenticationPermission(BasePermission):
    """Admin authentication permission condition check

    Args:
        (BasePermission) ([Django Method]): [Extend by django rest_framework permissions]

    Returns:
        [boolean]: [return true or false]
    """
    ADMIN_ONLY_AUTH_CLASSES = [rest_framework.authentication.BasicAuthentication,
                               rest_framework.authentication.SessionAuthentication]

    def has_permission(self, request, view):
        user = request.user
        if user and user.is_authenticated:
            return user.is_superuser or \
                not any(isinstance(request._authenticator, x)
                        for x in self.ADMIN_ONLY_AUTH_CLASSES)
        return False
