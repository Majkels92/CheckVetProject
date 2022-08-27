from django.urls import path
from . import views

urlpatterns = [
    path('klient/', views.main_klient, name='klient_home'),
]