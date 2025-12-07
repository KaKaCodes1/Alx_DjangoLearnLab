from django import forms
from .models import Book

class ExampleForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        required=True
    )
    author = forms.CharField(
        max_length=100,
        required=True,
    )