from rest_framework import viewsets

from . import models
from . import serializers


class FruitViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = serializers.FruitSerializer
    queryset = models.Fruit.objects.all().order_by('-pk')


class VegetableViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = serializers.VegetableSerializer
    queryset = models.Vegetable.objects.all().order_by('-pk')
