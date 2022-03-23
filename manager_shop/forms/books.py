from django.forms import forms, ModelForm
from django import forms

from manager_shop.models import Author, Publisher, Book


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, author):
        return "%s" % author.abbrev


class CustomMCF(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.name + ", " + obj.country


class AddBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'publicationDate', 'authors', 'publisher']

    # title = forms.CharField(label="Title", max_length=255)
    # price = forms.FloatField()
    publicationDate = forms.DateInput()
    authors = CustomMMCF(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    publisher = CustomMCF(
        queryset=Publisher.objects.all(),
    )


class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['abbrev', 'firstName', 'lastName']


class AddPublisher(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'country']


