from django.shortcuts import render, redirect
from django.contrib import messages
from apps.models.models import *
from .forms import *


# Create your views here.
def list_client(request):
    try:
        clients = Person.objects.filter(role__name='Client')
        context = {
            'title': 'List Clients',
            'clients': clients
        }
        return render(request, 'Veterinary/list.html', context)
    except Person.DoesNotExist:
        messages.warning(request, 'Client not found')
        return redirect('home')


def list_appointment(request):
    try:
        appointment = Appointment.objects.all()
        context = {
            'title': 'List Appointments',
            'appointment': appointment
        }
        return render(request, 'Veterinary/appointment.html', context)
    except Appointment.DoesNotExist:
        return redirect('list_client')


def register(request):
    try:
        role = Role.objects.get(name='Veterinary')
        form_veterinary = FormVeterinary(request.POST)
        form_account = FormAccount(request.POST)
        if request.method == 'POST':
            if form_veterinary.is_valid() and form_account.is_valid():
                data = form_veterinary.cleaned_data
                data_account = form_account.cleaned_data
                veterinary = Person(
                    role=role,
                    cedula=data.get('cedula'),
                    lastname=data.get('lastname'),
                    name=data.get('name'),
                    nro_phone=data.get('nro_phone'),
                )
                account = Account()
                account.email = data_account.get('email')
                account.set_password(data_account.get('password'))
                account.is_staff = False
                veterinary.save()
                account.person = veterinary
                account.save()
            messages.success(request, 'Veterinary create success')
            return redirect('list_appointment')
        context = {
            'title': 'Register Veterinary',
            'form_veterinary': form_veterinary,
        }
        return render(request, 'Veterinary/register.html', context)
    except Role.DoesNotExist:
        messages.warning(request, 'Role not found')
        return redirect('home')


def edit(request, **kwargs):
    try:
        external = kwargs.get('pk')
        person = Person.objects.get(pk=external)
        form_veterinary_edit = FormVeterinary(instance=person)
        if request.method == 'POST':
            form_veterinary_edit = FormVeterinary(request.POST, instance=person)
            if form_veterinary_edit.is_valid():
                data = form_veterinary_edit.cleaned_data
                person.lastname = data.get('lastname')
                person.name = data.get('name')
                person.nro_phone = data.get('nro_phone')
                person.save()
                messages.success(request, 'Veterinary updated success')
                return redirect('list_client')
        context = {
            'title': 'Register Veterinary',
            'form_veterinary': form_veterinary_edit,
        }
        return render(request, 'Veterinary/edit.html', context)
    except Role.DoesNotExist:
        messages.warning(request, 'Role not found')
        return redirect('home')
