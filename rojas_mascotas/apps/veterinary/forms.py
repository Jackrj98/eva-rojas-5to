from django import forms
from apps.models.models import *


class FormVeterinary(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['cedula', 'lastname', 'name', 'nro_phone']
        labels = {
            'cedula': 'Cedula',
            'lastname': 'LastName',
            'name': 'Name',
            'nro_phone': 'Phone',
        }
        widgets = {
            'cedula': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter number of cedula', 'maxlength': '10', }),
            'lastname': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter lastname', 'maxlength': '150'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter name', 'maxlength': '150'}),
            'nro_phone': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your phone', 'maxlength': '10'}),
        }


class FormAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Password',
        }
        widgets = {
            'email': forms.EmailInput(
                attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Enter email'}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'Enter password'}
            )
        }