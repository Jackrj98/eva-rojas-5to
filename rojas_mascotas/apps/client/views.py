from datetime import date

from django.shortcuts import render, redirect
from django.contrib import messages
from apps.models.models import *
from .forms import *


# Create your views here.
def list_pets(request):
    pets = Pets.objects.filter(person__account__email=request.user.email)
    context = {
        'title': 'Pets',
        'pets': pets
    }
    return render(request, 'Client/list.html', context)


def register(request):
    try:
        role = Role.objects.get(name='Client')
        form_client = FormClient(request.POST)
        form_account = FormAccount(request.POST)
        if request.method == 'POST':
            if form_client.is_valid() and form_account.is_valid():
                data = form_client.cleaned_data
                data_account = form_account.cleaned_data
                client = Person(
                    cedula=data.get('cedula'),
                    lastname=data.get('lastname'),
                    name=data.get('name'),
                    nro_phone=data.get('nro_phone'),
                    role=role
                )
                account = Account()
                account.email = data_account.get('email')
                account.set_password(data_account.get('password'))
                account.is_staff = False
                client.save()
                account.person = client
                account.save()
                messages.add_message(request, messages.SUCCESS, 'Client register success')
            else:
                messages.add_message(request, messages.ERROR, 'Client not register')
            return redirect('sign_in')
        context = {
            'title': 'Register Client',
            'form_client': form_client,
            'form_account': form_account
        }
        return render(request, 'Client/register.html', context)
    except Role.DoesNotExist:
        messages.warning(request, 'Role not found')
        return redirect('home')


def edit(request, **kwargs):
    external = kwargs.get('pk')

    person = Person.objects.get(pk=external)
    form_client = FormClientEdit(instance=person)
    if request.method == 'POST':
        form_client = FormClientEdit(request.POST, instance=person)
        if form_client.is_valid():
            person = form_client.save(commit=False)
            data = form_client.cleaned_data
            person.lastname = data.get('lastname')
            person.name = data.get('name')
            person.nro_phone = data.get('nro_phone')
            person.save()
            messages.add_message(request, messages.SUCCESS, 'Client updated success')
        else:
            messages.add_message(request, messages.ERROR, 'Client not register')
        return redirect(list_pets)
    context = {
        'title': 'Edit Client',
        'form_client_edit': form_client
    }
    return render(request, 'Client/edit.html', context)


def add_pet(request):
    try:
        person = Person.objects.get(account__email=request.user.email)
        form_pets = FormPets(request.POST)
        if request.method == 'POST':
            if form_pets.is_valid():
                data = form_pets.cleaned_data
                pet = Pets(
                    name=data.get('name'),
                    type=data.get('type'),
                    height=data.get('height'),
                    raza=data.get('raza'),
                    person=person
                )
                pet.save()
                return redirect('list_pets')
        context = {
            'form_pet': form_pets,
            'title': 'add pet'
        }
        return render(request, 'Client/register_pet.html', context)
    except Person.DoesNotExist:
        return redirect('list_pets')


def add_appointment(request):
    client = Person.objects.get(account__email=request.user.email)
    form_appointment = FormAppointment(request.POST)
    if request.method == 'POST':
        if form_appointment.is_valid():
            data = form_appointment.cleaned_data
            appointment = Appointment(
                date=data.get('date'),
                time=data.get('time'),
                person=client
            )
            appointment.save()
            return redirect('list_pets')
    context = {
        'title': 'Appointment',
        'form_appointment': form_appointment
    }
    return render(request, 'Client/register_appointment.html', context)
