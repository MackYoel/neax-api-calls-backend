from django.contrib import admin
from . import models


@admin.register(models.Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Vegetable)
class VegetableAdmin(admin.ModelAdmin):
    pass
