from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Shoe(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    color = models.CharField(max_length=60)
    size = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
