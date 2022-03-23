from django import forms

from manager_shop.models import Cloth, Vendor


class CustomMCF(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name + ", " + obj.address


class AddCloth(forms.ModelForm):
    class Meta:
        model = Cloth
        fields = ['name', 'color', 'style', 'size', 'vendor', 'price']

    vendor = CustomMCF(
        queryset=Vendor.objects.all()
    )


class AddVendor(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'country', 'address']
