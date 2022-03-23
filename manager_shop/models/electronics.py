from django.db import models

from manager_shop.models.shoes import Brand


class Size(models.Model):
    width = models.CharField(max_length=60)
    height = models.CharField(max_length=60)
    deep = models.CharField(max_length=60)
    weight = models.CharField(max_length=60)


class Electronic(models.Model):
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=60)
    wattage = models.CharField(max_length=60)
    size = models.OneToOneField(Size, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)


