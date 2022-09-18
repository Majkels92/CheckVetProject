from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.main_appointment, name='appointment_home'),
]