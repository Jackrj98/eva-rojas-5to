from django.contrib import admin
from .models import *


# Register your models here.
class AdminRole(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['name', 'status']
    search_fields = ['name']

    class Meta:
        model = Role


admin.site.register(Role, AdminRole)


class AdminPerson(admin.ModelAdmin):
    list_display = ['lastname', 'name', 'cedula', ]
    list_filter = ['name', 'cedula', ]
    search_fields = ['cedula', ]

    class Meta:
        model = Person


admin.site.register(Person, AdminPerson)


class AdminAccount(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'is_staff']
    list_filter = ['email']
    search_fields = ['email']

    class Meta:
        model = Account


admin.site.register(Account, AdminAccount)


class AdminPets(admin.ModelAdmin):
    list_display = ['name', 'raza', 'type', 'height', 'status']
    list_filter = ['name', 'raza', 'type']
    search_fields = ['name', 'raza', 'type']

    class Meta:
        model = Pets


admin.site.register(Pets, AdminPets)
