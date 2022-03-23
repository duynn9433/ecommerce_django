from django import forms

from manager_shop.models import MobilePhone, Memory, Producer


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s" % (obj.ram + '/' + obj.rom + '/' + str(obj.cardSlot))


class CustomMCF(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name + ", " + obj.address


class AddMobile(forms.ModelForm):
    class Meta:
        model = MobilePhone
        fields = ['name', 'display', 'platform', 'memories', 'producer']

    memories = CustomMMCF(
        queryset=Memory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    producer = CustomMCF(
        queryset=Producer.objects.all()
    )


class AddMemory(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['ram', 'rom', 'cardSlot']


class AddProducer(forms.ModelForm):
    class Meta:
        model = Producer
        fields = ['name', 'address']
