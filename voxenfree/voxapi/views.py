from django.shortcuts import render
from voxcore.models import Product
from rest_framework import viewsets
from voxapi.permissions import ProductPermission
from voxapi.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductPermission]
