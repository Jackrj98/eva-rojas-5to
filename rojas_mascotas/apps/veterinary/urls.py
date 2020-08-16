from django.urls import path, re_path
from . import views

urlpatterns = [
    path('client/', views.list_client, name='list_client'),
    path('appointment/', views.list_appointment, name='list_appointment'),
    path('register/', views.register, name='register_veterinary'),
    re_path('edit/(?P<id>[^/]+)', views.edit, name='edit_veterinary'),
]
