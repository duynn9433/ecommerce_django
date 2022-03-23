from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    address = models.CharField(max_length=255)


class Cloth(models.Model):
    name = models.CharField(max_length=60)
    color = models.CharField(max_length=60)
    style = models.CharField(max_length=60)
    size = models.CharField(max_length=255)
    price = models.FloatField()
    vendor = models.ForeignKey(Vendor,on_delete=models.RESTRICT)

    def str_vendor(self):
        return self.vendor.name


