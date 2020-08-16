from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from apps.models.models import *


def home_page(request):
    # person = Person.objects.get(account__email=request.user)
    if request.user.is_authenticated:
        print(request.user.person.role)
        return render(request, 'index.html', {'title': 'home'})
    return redirect('sign_in')
