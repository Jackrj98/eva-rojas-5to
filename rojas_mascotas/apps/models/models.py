from django import forms
from django.conf import settings
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    status = models.BooleanField(default=True, blank=False, null=False, editable=False)

    class Meta:
        db_table = 'role'
        verbose_name = 'role'
        verbose_name_plural = 'roles'
        ordering = ['name']

    def __str__(self):
        return self.name


class Person(models.Model):
    lastname = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=150, blank=False, null=False)
    cedula = models.CharField(max_length=10, blank=False, null=False, unique=True)
    nro_phone = models.CharField(max_length=10, blank=False, null=False)
    role = models.ForeignKey(Role, models.SET_NULL, null=True, related_name='persons')

    class Meta:
        db_table = 'person'
        verbose_name = 'person'
        verbose_name_plural = 'persons'
        ordering = ['pk']

    def __str__(self):
        string = str(self.name) + ' ' + str(self.lastname)
        return string


class Pets(models.Model):
    pet_list = (('D', 'Dog'), ('C', 'Cat'), ('B', 'Birds'), ('F', 'Fish'), ('H', 'Hamster'))
    name = models.CharField(max_length=150, blank=False, null=False)
    raza = models.CharField(max_length=150, blank=False, null=False)
    height = models.FloatField(blank=False, null=False)
    type = models.CharField(max_length=1, choices=pet_list, blank=False, null=False)
    status = models.BooleanField(default=True, blank=False, null=False, editable=False)
    person = models.ForeignKey(Person, related_name='pets', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'pets'
        verbose_name = 'pet'
        verbose_name_plural = 'pets'
        ordering = ['pk']

    def __str__(self):
        string = str(self.name) + ' ' + str(self.raza)
        return string


class Appointment(models.Model):
    date = models.DateField(blank=False, null=False)
    time = models.TimeField(blank=False, null=False)
    status = models.BooleanField(default=True, blank=False, null=False, editable=False)
    person = models.ForeignKey(Person, related_name='appointment', on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'appointment'
        verbose_name = 'appointment'
        verbose_name_plural = 'appointments'
        ordering = ['pk']

    def __str__(self):
        string = str(self.date) + ' ' + str(self.time)
        return string


class UserManager(BaseUserManager):
    def _create_user(self, email, password,
                     is_active, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email debe ser obligatorio')
        email = self.normalize_email(email)
        account = self.model(email=email, is_active=is_active,
                             is_superuser=is_superuser, **extra_fields)
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_user(self, email, password=False, **extra_fields):
        return self._create_user(email, password, True, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=200, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    person = models.OneToOneField(Person, models.SET_NULL, null=True, related_name='account')
    api_token = models.CharField(max_length=255)

    # intermediario entre trans de cada modelo, object managaer de cada modelo
    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.email

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.email

    class Meta:
        db_table = 'account'
        verbose_name = 'account'
        verbose_name_plural = 'accounts'
        ordering = ['pk']
