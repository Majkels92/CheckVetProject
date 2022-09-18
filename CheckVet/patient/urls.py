from django.urls import path
from . import views

urlpatterns = [
    path('patient/', views.main_patient, name='patient_home'),
]