from django.contrib.auth.models import Permission
from rest_framework import permissions, viewsets
from rest_framework.permissions import BasePermission, DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Product
from ..serializer import UserSerializer




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [CustomPermission]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
