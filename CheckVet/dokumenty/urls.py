from django.urls import path
from . import views

urlpatterns = [
    path('dokumenty/', views.main_dokumenty, name='dokumenty_home'),
]