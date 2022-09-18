from django.urls import path
from . import views

urlpatterns = [
    path('werehouse/', views.main_werehouse, name='werehouse_home'),
]