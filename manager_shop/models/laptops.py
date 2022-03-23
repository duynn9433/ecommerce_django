from django.db import models


# Create your models here.

class CPU(models.Model):
    model = models.CharField(max_length=255)
    family = models.CharField(max_length=60)
    frequency = models.CharField(max_length=10)
    core = models.IntegerField()
    thread = models.IntegerField()
    brand = models.CharField(max_length=60)


class RAM(models.Model):
    name = models.CharField(max_length=255)
    type =models.CharField(max_length=60)
    capacity = models.CharField(max_length=60)
    bus = models.CharField(max_length=60)


class Laptop(models.Model):
    name = models.CharField(max_length=255)
    cpu = models.ForeignKey(CPU, on_delete=models.RESTRICT)
    ram = models.ForeignKey(RAM, on_delete=models.RESTRICT)
    drive = models.CharField(max_length=255)

    def str_cpu(self):
        return self.cpu.model + ', ' + self.cpu.family + ', ' \
               + str(self.cpu.core) + ' cores-' + str(self.cpu.thread) + ' threads, ' + self.cpu.brand

    def str_ram(self):
        return self.ram.name + ', ' + self.ram.type + ', ' + self.ram.bus + ', ' + self.ram.capacity