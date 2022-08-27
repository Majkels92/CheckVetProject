from django.urls import path
from . import views

urlpatterns = [
    path('pacjent/', views.main_pacjent, name='pacjent_home'),
]