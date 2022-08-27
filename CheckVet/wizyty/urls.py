from django.urls import path
from . import views

urlpatterns = [
    path('wizyty/', views.main_wizyty, name='wizyty_home'),
]