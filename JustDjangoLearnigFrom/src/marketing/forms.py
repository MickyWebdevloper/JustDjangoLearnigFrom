import email
from django.forms import ModelForm
from . models import Signup
from django import forms


class SignupForm(forms.ModelForm):
    email = forms.CharField(
        label='', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Signup
        fields = ("email",)
