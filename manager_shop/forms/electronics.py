from django import forms


from manager_shop.models import Electronic, Size, Brand


class CustomMCF(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name + ", " + obj.country


class CustomMCFSize(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.width + "x" + obj.height + "x" + obj.deep + ", " + obj.weight


class AddElectronic(forms.ModelForm):
    class Meta:
        model = Electronic
        fields = ['name', 'type', 'wattage', 'size', 'brand']

    brand = CustomMCF(
        queryset=Brand.objects.all()
    )
    size = CustomMCFSize(
        queryset=Size.objects.all()
    )


class AddSize(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['width', 'height', 'deep', 'weight']
