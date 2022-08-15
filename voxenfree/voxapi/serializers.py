from rest_framework import serializers
from voxcore.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['type', 'name', 'set', 'description', 'price', 'stock']