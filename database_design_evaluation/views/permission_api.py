from django.contrib.auth.models import Permission
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from ..admin_permission import AdminAuthenticationPermission
from ..serializer import PermissionSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows permission to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (IsAuthenticated, AdminAuthenticationPermission,)
