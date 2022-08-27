from django.urls import path
from . import views

urlpatterns = [
    path('cennik/', views.main_cennik, name='cennik_home'),
]