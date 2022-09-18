from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_users, name='users_home'),
]