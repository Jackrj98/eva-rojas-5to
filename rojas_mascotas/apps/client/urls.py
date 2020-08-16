from django.urls import path, re_path
from . import views

urlpatterns = [
    path('pets/', views.list_pets, name='list_pets'),
    path('register', views.register, name='register_client'),
    re_path('edit/(?P<pk>[^/]+)', views.edit, name='edit_client'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('add_appointment/', views.add_appointment, name='add_appoinment'),
]
