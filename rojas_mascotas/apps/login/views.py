from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            email = request.POST['email']
            clave = request.POST['password']
            account = authenticate(email=email, password=clave)
            if account is not None:
                if account.is_active:
                    login(request, account)
                    return HttpResponseRedirect(reverse('home'))
                    # messages.warning(request, 'Te has identificado de forma correcta')
                else:
                    messages.warning(request, 'Usuario inactivo')
            else:
                messages.warning(request, 'Usuario y/o contraseña incorrecta')
    else:
        form_login = FormLogin()
    context = {
        'f': form_login,
    }
    return render(request, 'users/sign_in.html', context)


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
