from django.urls import path
from . import views

urlpatterns = [
    path('magazyn/', views.main_magazyn, name='magazyn_home'),
]