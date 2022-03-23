from django.db import models


# Create your models here.
class Memory(models.Model):
    ram = models.CharField(max_length=60)
    rom = models.CharField(max_length=60)
    cardSlot = models.IntegerField()


class Producer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class MobilePhone(models.Model):
    name = models.CharField(max_length=60)
    display = models.CharField(max_length=255)
    platform = models.CharField(max_length=60)
    memories = models.ManyToManyField(Memory)
    producer = models.ForeignKey(Producer, on_delete=models.RESTRICT)

    def str_memories(self):
        res = ''
        for m in self.memories.all():
            res += (m.ram + '/' + m.rom + '/' + str(m.cardSlot)) + ', '

        res = res[0:-2]
        return res

    def str_producer(self):
        return self.producer.name + '|' + self.producer.address
