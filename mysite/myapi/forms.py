
from django import forms
from .models import *
from django.forms import ModelForm


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
