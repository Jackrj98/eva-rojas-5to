from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_page, name='sign_in'),
    path('logout', views.logout_page, name='log_out'),
]