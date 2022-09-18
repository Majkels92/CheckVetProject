from django.urls import path
from . import views

urlpatterns = [
    path('client/', views.main_client, name='client_home'),
]