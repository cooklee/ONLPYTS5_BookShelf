from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from books.models import Author, Publisher, BooksOnLoan


def check_if_starts_with_big(val):
    if not val[0].isupper():
        raise ValidationError("Tytuł zaczynaj wielką literą")


def check_if_long(val):
    if len(val) < 4:
        raise ValidationError("Za krótki tytuł wyśil się")


class BookForm(forms.Form):
    title = forms.CharField(label="", validators=[check_if_starts_with_big, check_if_long],
                            widget=forms.TextInput(attrs=({'class': 'inputText', 'placeholder': 'Tytuł'})))
    author = forms.ModelChoiceField(queryset=Author.objects.all())


class AuthorForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()

    def clean(self):
        data = super().clean()
        if data.get('first_name', "").lower() == 'slawek' and data['last_name'].lower() == 'bo':
            raise ValidationError("tego pana nie obsługujemy")
        return data

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def clean(self):
        data = super().clean()
        if data.get('first_name', "").lower() == 'slawek' and data['last_name'].lower() == 'bo':
            raise ValidationError("tego pana nie obsługujemy")
        return data

class PublisherModelForm(forms.ModelForm):
    class Meta:
        model = Publisher
        exclude = ['city']
        labels = {
            'phone': 'Telefon',
            'name': 'Nazwa'
        }


class BooksOnLoanModelForm(forms.ModelForm):
    class Meta:
        model = BooksOnLoan
        exclude = ['user']
        widgets = {
            'books':forms.CheckboxSelectMultiple,
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
