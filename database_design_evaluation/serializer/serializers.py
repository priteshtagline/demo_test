from django.contrib.auth.models import User
from rest_framework import serializers

from ..models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_code']


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_permissions', 'groups')
