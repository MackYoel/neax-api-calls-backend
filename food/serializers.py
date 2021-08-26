from rest_framework import serializers

from . import models


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fruit
        fields = '__all__'


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vegetable
        fields = '__all__'