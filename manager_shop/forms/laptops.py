from django import forms

from manager_shop.models import Laptop, CPU, RAM


class CustomMCFcpu(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.model + ', ' + obj.family + ', ' \
               + str(obj.core) + ' cores-' + str(obj.thread) + ' threads, ' + obj.brand


class CustomMCFram(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name + ', ' + obj.type + ', ' + obj.bus + ', ' + obj.capacity


class AddLaptop(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ['name', 'cpu', 'ram', 'drive']

    cpu = CustomMCFcpu(
        queryset=CPU.objects.all()
    )
    ram = CustomMCFram(
        queryset=RAM.objects.all()
    )


class AddCPU(forms.ModelForm):
    class Meta:
        model = CPU
        fields = ['model', 'family', 'core', 'thread', 'frequency', 'brand']


class AddRAM(forms.ModelForm):
    class Meta:
        model = RAM
        fields = ['name', 'type', 'bus', 'capacity']
