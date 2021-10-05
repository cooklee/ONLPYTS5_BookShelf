from django import forms
from django.core.exceptions import ValidationError

from books.models import Author

def check_if_starts_with_big(val):
    if not val[0].isupper():
        raise ValidationError("Tytuł zaczynaj wielką literą")

def check_if_long(val):
    if len(val) < 4:
        raise ValidationError("Za krótki tytuł wyśil się")


class BookForm(forms.Form):
    title = forms.CharField(label="", validators=[check_if_starts_with_big, check_if_long], widget=forms.TextInput(attrs=({'class':'inputText','placeholder':'Tytuł'})))
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.RadioSelect)

class AuthorForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()