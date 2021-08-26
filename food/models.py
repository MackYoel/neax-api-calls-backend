from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Vegetable(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name
