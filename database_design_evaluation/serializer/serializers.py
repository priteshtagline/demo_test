# from django.contrib.auth.models import Group, User
from rest_framework import serializers
from ..models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_code']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']