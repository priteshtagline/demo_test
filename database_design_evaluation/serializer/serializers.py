from django.contrib.auth.models import Permission, User
from rest_framework import serializers

from ..models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_code']


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'user_permissions')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["user_permissions"] = GenreSerializer(
            instance.user_permissions.all(), many=True).data
        return rep
