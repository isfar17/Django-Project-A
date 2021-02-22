from django import forms
from django.forms import fields
from django.forms.widgets import HiddenInput
from .models import UserForm
from django.core import validators

class UserProfile(forms.ModelForm):
    botcheck=forms.CharField(required = False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])   

    class Meta():

        model=UserForm
        fields='__all__'