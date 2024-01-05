# forms.py
from django import forms

class ImageForm(forms.Form):
    images = forms.FileField()
