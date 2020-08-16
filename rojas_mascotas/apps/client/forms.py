from django import forms
from apps.models.models import *


class FormClient(forms.ModelForm):
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


class FormClientEdit(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['cedula', 'lastname', 'name', 'nro_phone', ]
        labels = {
            'cedula': 'Cedula',
            'lastname': 'LastName',
            'name': 'Name',
            'nro_phone': 'Phone',
        }
        widgets = {
            'cedula': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter number of cedula', 'maxlength': '10',
                       'readonly': 'true'}),
            'lastname': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter lastname', 'maxlength': '150'}),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter name', 'maxlength': '150'}),
            'nro_phone': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your phone', 'maxlength': '10'}),
        }


class FormPets(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['name', 'raza', 'height', 'type']
        labels = {
            'name': 'name',
            'raza': 'raza',
            'height': 'height',
            'type': 'type',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter of name', 'maxlength': '150'}),
            'raza': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter lastname', 'maxlength': '150'}),
            'height': forms.TextInput(
                attrs={'class': 'form-control', 'type': 'decimal', 'placeholder': 'Enter name'}),
            'type': forms.Select(
                attrs={'class': 'form-control'}),
        }


class FormAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']
        labels = {
            'date': 'date',
            'time': 'time'
        }
        widgets = {
            'date': forms.DateTimeInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter of name', 'type': 'date'}),
            'time': forms.TimeInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter lastname', 'type': 'time'}),
        }
